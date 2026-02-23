"""
Script d'optimisation ciblé — SAE-125

Questions testées :
1. balanced vs non-balanced pour LogReg sur embeddings DistilBERT
2. Quel C est optimal pour chaque config ?
3. Impact taille échantillon (10K vs 25K vs 50K) sur TF-IDF + LogReg
4. Comparaison TF-IDF 50K : tous les modèles
"""

import sys
import os
import time
import warnings

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, accuracy_score

from src.constants import stars_to_polarity

RANDOM_STATE = 42
RESULTS = []


def run_experiment(name, model, params, X_train, y_train, X_val, y_val,
                   task, features='', sample_size='', cv=3):
    """GridSearchCV + évaluation rapide."""
    t0 = time.time()
    gs = GridSearchCV(model, params, cv=cv, scoring='f1_macro',
                      n_jobs=-1, refit=True)
    gs.fit(X_train, y_train)

    y_pred = gs.best_estimator_.predict(X_val)
    y_pred_tr = gs.best_estimator_.predict(X_train)
    f1 = f1_score(y_val, y_pred, average='macro', zero_division=0)
    acc = accuracy_score(y_val, y_pred)
    gap = accuracy_score(y_train, y_pred_tr) - acc
    elapsed = time.time() - t0

    RESULTS.append({
        'Modèle': name, 'Features': features, 'Sample': sample_size,
        'Tâche': task,
        'F1 Macro': round(f1, 4), 'Accuracy': round(acc, 4),
        'Overfit Gap': round(gap, 4), 'CV F1': round(gs.best_score_, 4),
        'Best Params': str(gs.best_params_), 'Temps (s)': round(elapsed, 1),
    })
    print(f"  {name:30s} | {task:10s} | F1={f1:.4f} | Acc={acc:.4f} | "
          f"Gap={gap:+.4f} | {gs.best_params_} | {elapsed:.0f}s", flush=True)
    return gs.best_estimator_


# ==========================================================================
# CHARGEMENT DES DONNÉES
# ==========================================================================
print("Chargement des embeddings DistilBERT...", flush=True)
X_all = np.load('outputs/distilbert_embeddings.npy')
y_pol_all = np.load('outputs/distilbert_labels_polarity.npy')
y_sc_all = np.load('outputs/distilbert_labels_score.npy')

# Split 80/10/10
X_train, X_temp, yp_tr, yp_tmp, ys_tr, ys_tmp = train_test_split(
    X_all, y_pol_all, y_sc_all, test_size=0.20,
    random_state=RANDOM_STATE, stratify=y_pol_all
)
X_val, X_test, yp_va, yp_te, ys_va, ys_te = train_test_split(
    X_temp, yp_tmp, ys_tmp, test_size=0.50,
    random_state=RANDOM_STATE, stratify=yp_tmp
)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s = scaler.transform(X_val)
print(f"Train: {len(X_train)} | Val: {len(X_val)} | Test: {len(X_test)}", flush=True)


# ==========================================================================
# TEST 1 : balanced vs non-balanced — LogReg sur embeddings
# ==========================================================================
print("\n" + "=" * 80)
print("TEST 1 : class_weight balanced vs None — LogReg + Embeddings")
print("=" * 80, flush=True)

C_values = [0.001, 0.01, 0.1, 1, 10, 100]

for balanced in [None, 'balanced']:
    label = f"LogReg ({'balanced' if balanced else 'none'})"
    print(f"\n--- {label} ---", flush=True)
    model = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE,
                               class_weight=balanced, solver='lbfgs')
    params = {'C': C_values}

    for y_tr, y_va, task in [(yp_tr, yp_va, 'Polarité'), (ys_tr, ys_va, 'Score')]:
        run_experiment(label, model, params, X_train_s, y_tr, X_val_s, y_va,
                       task, features='Embeddings LLM', sample_size='50K')


# ==========================================================================
# TEST 2 : balanced vs non-balanced — LinearSVC sur embeddings
# ==========================================================================
print("\n" + "=" * 80)
print("TEST 2 : class_weight balanced vs None — LinearSVC + Embeddings")
print("=" * 80, flush=True)

for balanced in [None, 'balanced']:
    label = f"LinearSVC ({'balanced' if balanced else 'none'})"
    print(f"\n--- {label} ---", flush=True)
    model = LinearSVC(random_state=RANDOM_STATE, max_iter=2000,
                      dual='auto', class_weight=balanced)
    params = {'C': [0.001, 0.01, 0.1, 1, 10]}

    for y_tr, y_va, task in [(yp_tr, yp_va, 'Polarité'), (ys_tr, ys_va, 'Score')]:
        run_experiment(label, model, params, X_train_s, y_tr, X_val_s, y_va,
                       task, features='Embeddings LLM', sample_size='50K')


# ==========================================================================
# TEST 3 : GaussianNB sur embeddings
# ==========================================================================
print("\n" + "=" * 80)
print("TEST 3 : GaussianNB + Embeddings")
print("=" * 80, flush=True)

model = GaussianNB()
params = {'var_smoothing': [1e-11, 1e-10, 1e-9, 1e-8, 1e-7]}

for y_tr, y_va, task in [(yp_tr, yp_va, 'Polarité'), (ys_tr, ys_va, 'Score')]:
    run_experiment('GaussianNB', model, params, X_train_s, y_tr, X_val_s, y_va,
                   task, features='Embeddings LLM', sample_size='50K')


# ==========================================================================
# TEST 4 : Impact taille échantillon — TF-IDF + LogReg
# ==========================================================================
print("\n" + "=" * 80)
print("TEST 4 : Impact taille échantillon — TF-IDF + LogReg (sans balanced)")
print("=" * 80, flush=True)

df = pd.read_parquet('data/cleaned/reviews_clean.parquet', columns=['text', 'stars'])
df = df.dropna(subset=['text', 'stars'])
df['polarity'] = df['stars'].apply(stars_to_polarity)
print(f"Dataset complet : {len(df):,} reviews", flush=True)

for sample_size in [10_000, 25_000, 50_000]:
    print(f"\n--- {sample_size:,} samples ---", flush=True)
    df_s = df.sample(n=sample_size, random_state=RANDOM_STATE)

    tfidf = TfidfVectorizer(max_features=20_000, ngram_range=(1, 2),
                            min_df=3, max_df=0.95, sublinear_tf=True)
    X = tfidf.fit_transform(df_s['text'])
    y_pol = df_s['polarity'].values
    y_sc = df_s['stars'].values.astype(int)

    X_tr, X_tmp, yp_tr_t, yp_tmp_t, ys_tr_t, ys_tmp_t = train_test_split(
        X, y_pol, y_sc, test_size=0.20, random_state=RANDOM_STATE, stratify=y_pol
    )
    X_va, _, yp_va_t, _, ys_va_t, _ = train_test_split(
        X_tmp, yp_tmp_t, ys_tmp_t, test_size=0.50,
        random_state=RANDOM_STATE, stratify=yp_tmp_t
    )

    model = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE, solver='lbfgs')
    params = {'C': [0.1, 1, 10, 50]}

    for y_tr_t, y_va_t, task in [
        (yp_tr_t, yp_va_t, 'Polarité'),
        (ys_tr_t, ys_va_t, 'Score'),
    ]:
        run_experiment('LogReg', model, params, X_tr, y_tr_t, X_va, y_va_t,
                       task, features='TF-IDF', sample_size=f'{sample_size//1000}K')


# ==========================================================================
# TEST 5 : Tous modèles sur TF-IDF 50K (sans balanced pour NB et comparaison)
# ==========================================================================
print("\n" + "=" * 80)
print("TEST 5 : Comparaison tous modèles — TF-IDF 50K")
print("=" * 80, flush=True)

# Réutiliser le dernier split TF-IDF 50K du test 4
tfidf_models = {
    'LinearSVC': {
        'model': LinearSVC(random_state=RANDOM_STATE, max_iter=2000, dual='auto'),
        'params': {'C': [0.1, 1, 10]},
    },
    'MultinomialNB': {
        'model': MultinomialNB(),
        'params': {'alpha': [0.01, 0.1, 0.5, 1.0]},
    },
}

for name, config in tfidf_models.items():
    print(f"\n--- {name} ---", flush=True)
    for y_tr_t, y_va_t, task in [
        (yp_tr_t, yp_va_t, 'Polarité'),
        (ys_tr_t, ys_va_t, 'Score'),
    ]:
        run_experiment(name, config['model'], config['params'],
                       X_tr, y_tr_t, X_va, y_va_t, task,
                       features='TF-IDF', sample_size='50K')


# ==========================================================================
# RÉSUMÉ FINAL
# ==========================================================================
print("\n" + "=" * 80)
print("RÉSUMÉ COMPLET — TOUS LES RÉSULTATS")
print("=" * 80, flush=True)

df_results = pd.DataFrame(RESULTS)

for task in ['Polarité', 'Score']:
    df_task = df_results[df_results['Tâche'] == task].sort_values(
        'F1 Macro', ascending=False)
    print(f"\n--- TOP MODÈLES — {task} ---")
    for _, row in df_task.iterrows():
        print(f"  {row['Modèle']:30s} {row['Features']:15s} {row['Sample']:5s} | "
              f"F1={row['F1 Macro']:.4f} | Acc={row['Accuracy']:.4f} | "
              f"Gap={row['Overfit Gap']:+.4f}")

# Comparaison balanced vs non-balanced
print("\n--- COMPARAISON balanced vs non-balanced (Embeddings LLM) ---")
emb = df_results[df_results['Features'] == 'Embeddings LLM']
for task in ['Polarité', 'Score']:
    print(f"\n  {task}:")
    for _, row in emb[emb['Tâche'] == task].sort_values('F1 Macro', ascending=False).iterrows():
        print(f"    {row['Modèle']:30s} | F1={row['F1 Macro']:.4f} | "
              f"Acc={row['Accuracy']:.4f} | {row['Best Params']}")

# Impact taille échantillon
print("\n--- IMPACT TAILLE ÉCHANTILLON (TF-IDF + LogReg) ---")
tfidf_lr = df_results[(df_results['Features'] == 'TF-IDF') &
                       (df_results['Modèle'] == 'LogReg')]
for task in ['Polarité', 'Score']:
    print(f"\n  {task}:")
    for _, row in tfidf_lr[tfidf_lr['Tâche'] == task].iterrows():
        print(f"    {row['Sample']:5s} | F1={row['F1 Macro']:.4f} | "
              f"Acc={row['Accuracy']:.4f} | {row['Best Params']}")

# Sauvegarder
df_results.to_csv('outputs/optimization_results.csv', index=False)
print(f"\nRésultats : outputs/optimization_results.csv ({len(RESULTS)} expériences)")
