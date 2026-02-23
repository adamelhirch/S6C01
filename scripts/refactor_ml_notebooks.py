"""Script de génération des notebooks ML refactorisés (Phase 2)."""
import nbformat as nbf

def md(source):
    return nbf.v4.new_markdown_cell(source)

def code(source):
    return nbf.v4.new_code_cell(source)

def save_nb(cells, path):
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata['kernelspec'] = {
        'display_name': 'Python 3',
        'language': 'python',
        'name': 'python3'
    }
    with open(path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f'  ✓ {path}')


# ============================================================
# 01-ml-tfidf.ipynb
# ============================================================
def gen_01():
    return [
        md("""# Classification ML Classique sur features TF-IDF

Ce notebook entraîne et compare 4 algorithmes ML sur une représentation **TF-IDF** des avis Yelp :
Logistic Regression, LinearSVC, Random Forest, Naive Bayes.

**Deux tâches** : Polarité (3 classes) et Score (1-5 étoiles)."""),

        code("""import sys
sys.path.insert(0, '../..')

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import warnings
warnings.filterwarnings('ignore')

from src.constants import POLARITY_NAMES, SCORE_NAMES
from src.ml_utils import load_and_prepare, split_data, get_param_grids, tune_and_evaluate
from src.evaluation import plot_confusion, print_report
from src import setup_plot_style

setup_plot_style()
MODELS_DIR = '../../models/'
os.makedirs(MODELS_DIR, exist_ok=True)"""),

        md("## 1. Chargement et Préparation"),

        code("""df = load_and_prepare()
data = split_data(df['text'], df['polarity'], df['stars'])
print(f"Train: {len(data['X_train'])} | Val: {len(data['X_val'])} | Test: {len(data['X_test'])}")"""),

        md("""## 2. Vectorisation TF-IDF

Ajustement uniquement sur l'ensemble d'entraînement (pas de data leakage)."""),

        code("""vectorizer = TfidfVectorizer(max_features=10_000, min_df=5, max_df=0.7, ngram_range=(1, 2))

X_train = vectorizer.fit_transform(data['X_train'])
X_val = vectorizer.transform(data['X_val'])
X_test = vectorizer.transform(data['X_test'])

print(f"Matrice TF-IDF : {X_train.shape}")"""),

        md("## 3. Classification — Score (1-5 étoiles)"),

        code("""grids = get_param_grids()
results_sc, models_sc, preds_sc = tune_and_evaluate(
    grids, X_train, data['y_sc_train'], X_val, data['y_sc_val']
)"""),

        code("""results_sc_df = pd.DataFrame(results_sc).T
display(results_sc_df.sort_values('f1', ascending=False))

best_sc = results_sc_df['f1'].idxmax()
print(f"\\nMeilleur modèle Score : {best_sc} (F1={results_sc_df.loc[best_sc, 'f1']:.4f})")

plot_confusion(data['y_sc_val'], preds_sc[best_sc], SCORE_NAMES, f'{best_sc} — Score')
print_report(data['y_sc_val'], preds_sc[best_sc], SCORE_NAMES, f'{best_sc} — Score')"""),

        md("## 4. Classification — Polarité (3 classes)"),

        code("""grids_pol = get_param_grids()
results_pol, models_pol, preds_pol = tune_and_evaluate(
    grids_pol, X_train, data['y_pol_train'], X_val, data['y_pol_val']
)"""),

        code("""results_pol_df = pd.DataFrame(results_pol).T
display(results_pol_df.sort_values('f1', ascending=False))

best_pol = results_pol_df['f1'].idxmax()
print(f"\\nMeilleur modèle Polarité : {best_pol} (F1={results_pol_df.loc[best_pol, 'f1']:.4f})")

plot_confusion(data['y_pol_val'], preds_pol[best_pol], POLARITY_NAMES, f'{best_pol} — Polarité')
print_report(data['y_pol_val'], preds_pol[best_pol], POLARITY_NAMES, f'{best_pol} — Polarité')"""),

        md("## 5. Test Final & Sauvegarde"),

        code("""# Évaluation sur le test set
print_report(data['y_sc_test'], models_sc[best_sc].predict(X_test),
             SCORE_NAMES, f'{best_sc} — Score (Test)')
print_report(data['y_pol_test'], models_pol[best_pol].predict(X_test),
             POLARITY_NAMES, f'{best_pol} — Polarité (Test)')

# Sauvegarde
joblib.dump(models_sc[best_sc], os.path.join(MODELS_DIR, 'best_tfidf_classifier.pkl'))
joblib.dump(models_pol[best_pol], os.path.join(MODELS_DIR, 'best_tfidf_polarity.pkl'))
joblib.dump(vectorizer, os.path.join(MODELS_DIR, 'tfidf_vectorizer.pkl'))
print(f"\\nModèles sauvegardés dans {MODELS_DIR}")"""),
    ]


# ============================================================
# 02-ml-ngram.ipynb
# ============================================================
def gen_02():
    return [
        md("""# Classification ML Classique sur features N-Grammes

Ce notebook entraîne et compare 4 algorithmes ML sur une représentation **N-grammes** (CountVectorizer) des avis Yelp :
Logistic Regression, LinearSVC, Random Forest, Naive Bayes.

**Deux tâches** : Polarité (3 classes) et Score (1-5 étoiles)."""),

        code("""import sys
sys.path.insert(0, '../..')

import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import warnings
warnings.filterwarnings('ignore')

from src.constants import POLARITY_NAMES, SCORE_NAMES
from src.ml_utils import load_and_prepare, split_data, get_param_grids, tune_and_evaluate
from src.evaluation import plot_confusion, print_report
from src import setup_plot_style

setup_plot_style()
MODELS_DIR = '../../models/'
os.makedirs(MODELS_DIR, exist_ok=True)"""),

        md("## 1. Chargement et Préparation"),

        code("""df = load_and_prepare()
data = split_data(df['text'], df['polarity'], df['stars'])
print(f"Train: {len(data['X_train'])} | Val: {len(data['X_val'])} | Test: {len(data['X_test'])}")"""),

        md("""## 2. Vectorisation N-Grammes

CountVectorizer avec unigrammes et bigrammes, ajusté uniquement sur le train."""),

        code("""vectorizer = CountVectorizer(max_features=10_000, min_df=5, max_df=0.7, ngram_range=(1, 2))

X_train = vectorizer.fit_transform(data['X_train'])
X_val = vectorizer.transform(data['X_val'])
X_test = vectorizer.transform(data['X_test'])

print(f"Matrice N-grammes : {X_train.shape}")"""),

        md("## 3. Classification — Score (1-5 étoiles)"),

        code("""grids = get_param_grids()
results_sc, models_sc, preds_sc = tune_and_evaluate(
    grids, X_train, data['y_sc_train'], X_val, data['y_sc_val']
)"""),

        code("""results_sc_df = pd.DataFrame(results_sc).T
display(results_sc_df.sort_values('f1', ascending=False))

best_sc = results_sc_df['f1'].idxmax()
print(f"\\nMeilleur modèle Score : {best_sc} (F1={results_sc_df.loc[best_sc, 'f1']:.4f})")

plot_confusion(data['y_sc_val'], preds_sc[best_sc], SCORE_NAMES, f'{best_sc} — Score')
print_report(data['y_sc_val'], preds_sc[best_sc], SCORE_NAMES, f'{best_sc} — Score')"""),

        md("## 4. Classification — Polarité (3 classes)"),

        code("""grids_pol = get_param_grids()
results_pol, models_pol, preds_pol = tune_and_evaluate(
    grids_pol, X_train, data['y_pol_train'], X_val, data['y_pol_val']
)"""),

        code("""results_pol_df = pd.DataFrame(results_pol).T
display(results_pol_df.sort_values('f1', ascending=False))

best_pol = results_pol_df['f1'].idxmax()
print(f"\\nMeilleur modèle Polarité : {best_pol} (F1={results_pol_df.loc[best_pol, 'f1']:.4f})")

plot_confusion(data['y_pol_val'], preds_pol[best_pol], POLARITY_NAMES, f'{best_pol} — Polarité')
print_report(data['y_pol_val'], preds_pol[best_pol], POLARITY_NAMES, f'{best_pol} — Polarité')"""),

        md("## 5. Test Final & Sauvegarde"),

        code("""# Évaluation sur le test set
print_report(data['y_sc_test'], models_sc[best_sc].predict(X_test),
             SCORE_NAMES, f'{best_sc} — Score (Test)')
print_report(data['y_pol_test'], models_pol[best_pol].predict(X_test),
             POLARITY_NAMES, f'{best_pol} — Polarité (Test)')

# Sauvegarde
joblib.dump(models_sc[best_sc], os.path.join(MODELS_DIR, 'best_ngram_classifier.pkl'))
joblib.dump(models_pol[best_pol], os.path.join(MODELS_DIR, 'best_ngram_polarity.pkl'))
joblib.dump(vectorizer, os.path.join(MODELS_DIR, 'count_vectorizer.pkl'))
print(f"\\nModèles sauvegardés dans {MODELS_DIR}")"""),
    ]


# ============================================================
# 03-ml-llm.ipynb
# ============================================================
def gen_03():
    return [
        md("""# Classification ML sur Embeddings LLM (DistilBERT)

**SAE-117** — 4 algorithmes ML sur embeddings DistilBERT pré-calculés (768 dimensions).

**Corrections vs version précédente :**
- Split 80/10/10 (au lieu de 80/20)
- Métriques en `macro` averaging (au lieu de `weighted`)
- GridSearchCV pour tous les modèles
- GaussianNB (embeddings continus, pas de MultinomialNB)"""),

        code("""import sys
sys.path.insert(0, '../..')

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

from src.constants import RANDOM_STATE, POLARITY_NAMES, SCORE_NAMES
from src.ml_utils import split_data, get_param_grids, tune_and_evaluate
from src.evaluation import plot_confusion, print_report
from src import setup_plot_style

setup_plot_style()"""),

        md("## 1. Chargement des embeddings DistilBERT"),

        code("""X = np.load('../../outputs/distilbert_embeddings.npy')
y_polarity = np.load('../../outputs/distilbert_labels_polarity.npy')
y_score = np.load('../../outputs/distilbert_labels_score.npy')

print(f'Embeddings : {X.shape}')
print(f'\\nPolarité :')
for label, name in enumerate(POLARITY_NAMES):
    n = (y_polarity == label).sum()
    print(f'  {label} ({name}): {n:,} ({n/len(y_polarity)*100:.1f}%)')
print(f'\\nScore :')
for star in range(1, 6):
    n = (y_score == star).sum()
    print(f'  {star}★: {n:,} ({n/len(y_score)*100:.1f}%)')"""),

        md("""## 2. Split 80/10/10 & Standardisation

Split stratifié sur la polarité, puis standardisation (importante pour LogReg et SVM)."""),

        code("""data = split_data(X, y_polarity, y_score)
print(f"Train: {len(data['X_train'])} | Val: {len(data['X_val'])} | Test: {len(data['X_test'])}")

# Standardisation (RF est scale-invariant, donc pas de souci)
scaler = StandardScaler()
X_train = scaler.fit_transform(data['X_train'])
X_val = scaler.transform(data['X_val'])
X_test = scaler.transform(data['X_test'])

print(f'Standardisation appliquée (mean={X_train.mean():.6f}, std={X_train.std():.6f})')"""),

        md("## 3. Classification — Polarité (3 classes)"),

        code("""# GaussianNB car les embeddings sont continus (pas de MultinomialNB)
grids = get_param_grids(use_gaussian_nb=True)
results_pol, models_pol, preds_pol = tune_and_evaluate(
    grids, X_train, data['y_pol_train'], X_val, data['y_pol_val']
)"""),

        code("""results_pol_df = pd.DataFrame(results_pol).T
display(results_pol_df.sort_values('f1', ascending=False))

best_pol = results_pol_df['f1'].idxmax()
print(f"\\nMeilleur modèle Polarité : {best_pol} (F1 Macro={results_pol_df.loc[best_pol, 'f1']:.4f})")

plot_confusion(data['y_pol_val'], preds_pol[best_pol], POLARITY_NAMES, f'{best_pol} — Polarité (LLM)')
print_report(data['y_pol_val'], preds_pol[best_pol], POLARITY_NAMES, f'{best_pol} — Polarité')"""),

        md("## 4. Classification — Score (1-5 étoiles)"),

        code("""grids_sc = get_param_grids(use_gaussian_nb=True)
results_sc, models_sc, preds_sc = tune_and_evaluate(
    grids_sc, X_train, data['y_sc_train'], X_val, data['y_sc_val']
)"""),

        code("""results_sc_df = pd.DataFrame(results_sc).T
display(results_sc_df.sort_values('f1', ascending=False))

best_sc = results_sc_df['f1'].idxmax()
print(f"\\nMeilleur modèle Score : {best_sc} (F1 Macro={results_sc_df.loc[best_sc, 'f1']:.4f})")

plot_confusion(data['y_sc_val'], preds_sc[best_sc], SCORE_NAMES, f'{best_sc} — Score (LLM)')
print_report(data['y_sc_val'], preds_sc[best_sc], SCORE_NAMES, f'{best_sc} — Score')"""),

        md("## 5. Test Final"),

        code("""print_report(data['y_pol_test'], models_pol[best_pol].predict(X_test),
             POLARITY_NAMES, f'{best_pol} — Polarité (Test)')
print_report(data['y_sc_test'], models_sc[best_sc].predict(X_test),
             SCORE_NAMES, f'{best_sc} — Score (Test)')

print('\\n✅ Notebook SAE-117 terminé')
print(f'   Meilleur Polarité : {best_pol} (F1 Macro={results_pol_df.loc[best_pol, "f1"]:.4f})')
print(f'   Meilleur Score    : {best_sc} (F1 Macro={results_sc_df.loc[best_sc, "f1"]:.4f})')"""),
    ]


# ============================================================
# 04-selection-variables.ipynb
# ============================================================
def gen_04():
    return [
        md("""# Sélection de Variables (Feature Importance)

Analyse de l'importance des features TF-IDF via Random Forest, sélection d'un sous-ensemble optimal, et comparaison avant/après.

**Checklist SAE-118 :**
- Feature importance (Random Forest)
- Visualisation top-N features
- Sélection de sous-ensembles (500, 1000, 2000)
- Comparaison performance avant/après"""),

        code("""import sys
sys.path.insert(0, '../..')

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report
import joblib
import warnings
warnings.filterwarnings('ignore')

from src.constants import RANDOM_STATE, SCORE_NAMES, POLARITY_NAMES
from src.ml_utils import load_and_prepare, split_data
from src.evaluation import plot_confusion, print_report
from src import setup_plot_style

setup_plot_style()
MODELS_DIR = '../../models/'
os.makedirs(MODELS_DIR, exist_ok=True)"""),

        md("## 1. Chargement et Préparation"),

        code("""df = load_and_prepare()
data = split_data(df['text'], df['polarity'], df['stars'])
print(f"Train: {len(data['X_train'])} | Val: {len(data['X_val'])} | Test: {len(data['X_test'])}")"""),

        md("## 2. Vectorisation TF-IDF (baseline 10k features)"),

        code("""N_FEATURES_FULL = 10_000

vectorizer_full = TfidfVectorizer(
    max_features=N_FEATURES_FULL, min_df=5, max_df=0.7, ngram_range=(1, 2)
)

X_train_full = vectorizer_full.fit_transform(data['X_train'])
X_val_full = vectorizer_full.transform(data['X_val'])
X_test_full = vectorizer_full.transform(data['X_test'])

feature_names = vectorizer_full.get_feature_names_out()
print(f'Matrice TF-IDF (train) : {X_train_full.shape}')"""),

        md("## 3. Modèle Baseline (toutes les features)"),

        code("""clf_baseline = LogisticRegression(max_iter=500, random_state=RANDOM_STATE, n_jobs=-1)
clf_baseline.fit(X_train_full, data['y_sc_train'])

y_pred_baseline = clf_baseline.predict(X_val_full)
acc_baseline = accuracy_score(data['y_sc_val'], y_pred_baseline)
f1_baseline = f1_score(data['y_sc_val'], y_pred_baseline, average='macro')

print(f'=== BASELINE ({N_FEATURES_FULL} features) ===')
print(f'Accuracy (val) : {acc_baseline:.4f}')
print(f'F1 Macro (val) : {f1_baseline:.4f}')"""),

        md("## 4. Feature Importance (Random Forest)"),

        code("""print('Entraînement Random Forest pour feature importance...')
rf = RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE, n_jobs=-1)
rf.fit(X_train_full, data['y_sc_train'])

importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]
print(f'Feature importance calculée sur {len(importances)} features.')"""),

        md("## 5. Visualisation des Top-N Features"),

        code("""TOP_N = 30
top_features = [feature_names[i] for i in indices[:TOP_N]]
top_scores = importances[indices[:TOP_N]]

fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(range(TOP_N), top_scores[::-1], color='steelblue', edgecolor='white')
ax.set_yticks(range(TOP_N))
ax.set_yticklabels(top_features[::-1], fontsize=10)
ax.set_xlabel('Importance (Random Forest)')
ax.set_title(f'Top {TOP_N} Features les Plus Importantes', fontweight='bold')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()"""),

        code("""# Distribution cumulée
sorted_imp = np.sort(importances)[::-1]
cumulative = np.cumsum(sorted_imp)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(sorted_imp[:500], color='steelblue')
axes[0].set_xlabel('Rang de la feature')
axes[0].set_ylabel('Importance')
axes[0].set_title("Distribution de l'importance (top 500)")
axes[0].grid(alpha=0.3)

axes[1].plot(cumulative, color='darkorange')
for t in [0.5, 0.7, 0.9, 0.95]:
    n = np.searchsorted(cumulative, t) + 1
    axes[1].axhline(t, color='gray', linestyle='--', linewidth=0.8)
    axes[1].annotate(f'{t*100:.0f}% -> {n} feat.', xy=(n, t),
                     xytext=(n + 200, t - 0.03), fontsize=8,
                     arrowprops=dict(arrowstyle='->', color='gray'))
axes[1].set_xlabel('Nombre de features')
axes[1].set_ylabel('Importance cumulée')
axes[1].set_title('Importance Cumulée')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()"""),

        md("## 6. Sélection de Sous-ensembles & Comparaison"),

        code("""K_VALUES = [500, 1000, 2000]
results = {}

for k in K_VALUES:
    top_k_idx = indices[:k]
    X_tr_k = X_train_full[:, top_k_idx]
    X_vl_k = X_val_full[:, top_k_idx]

    clf_k = LogisticRegression(max_iter=500, random_state=RANDOM_STATE, n_jobs=-1)
    clf_k.fit(X_tr_k, data['y_sc_train'])

    y_pred_k = clf_k.predict(X_vl_k)
    acc_k = accuracy_score(data['y_sc_val'], y_pred_k)
    f1_k = f1_score(data['y_sc_val'], y_pred_k, average='macro')

    results[f'Top-{k}'] = {
        'n_features': k, 'accuracy': acc_k, 'f1_macro': f1_k,
        'clf': clf_k, 'top_k_idx': top_k_idx
    }
    print(f'Top-{k:5d} features | Acc: {acc_k:.4f} | F1 Macro: {f1_k:.4f}')

results['Baseline (10k)'] = {
    'n_features': N_FEATURES_FULL, 'accuracy': acc_baseline, 'f1_macro': f1_baseline
}"""),

        code("""# Tableau comparatif
summary = pd.DataFrame([
    {'Config': name, 'Features': v['n_features'],
     'Accuracy': round(v['accuracy'], 4), 'F1 Macro': round(v['f1_macro'], 4),
     'Réduction (%)': round((1 - v['n_features'] / N_FEATURES_FULL) * 100, 1)}
    for name, v in results.items()
])
display(summary.sort_values('F1 Macro', ascending=False).reset_index(drop=True))

# Visualisation
configs = list(results.keys())
f1s = [results[c]['f1_macro'] for c in configs]
accs = [results[c]['accuracy'] for c in configs]

fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(configs))
ax.bar(x - 0.15, accs, 0.3, label='Accuracy', color='steelblue', alpha=0.85)
ax.bar(x + 0.15, f1s, 0.3, label='F1 Macro', color='darkorange', alpha=0.85)
ax.set_xticks(x)
ax.set_xticklabels(configs, rotation=15, ha='right')
ax.set_ylim(0, 1)
ax.set_ylabel('Score')
ax.set_title('Performance par Nombre de Features')
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()"""),

        md("## 7. Meilleur Sous-ensemble & Test Final"),

        code("""# Meilleure config réduite
reduced = {k: v for k, v in results.items() if k != 'Baseline (10k)'}
best_name = max(reduced, key=lambda k: reduced[k]['f1_macro'])
best = reduced[best_name]

print(f'=== MEILLEURE CONFIG : {best_name} ===')
print(f'Features   : {best["n_features"]}')
print(f'Accuracy   : {best["accuracy"]:.4f}')
print(f'F1 Macro   : {best["f1_macro"]:.4f}')
print(f'Réduction  : {(1 - best["n_features"] / N_FEATURES_FULL) * 100:.1f}%')
print(f'\\nΔ F1 vs baseline : {best["f1_macro"] - f1_baseline:+.4f}')

# Test final
X_test_k = X_test_full[:, best['top_k_idx']]
print_report(data['y_sc_test'], best['clf'].predict(X_test_k),
             SCORE_NAMES, f'{best_name} — Score (Test)')
plot_confusion(data['y_sc_test'], best['clf'].predict(X_test_k),
               SCORE_NAMES, f'{best_name} — Score (Test)')"""),

        md("## 8. Sauvegarde"),

        code("""selected_names = feature_names[best['top_k_idx']]

joblib.dump(best['clf'], os.path.join(MODELS_DIR, 'best_selected_classifier.pkl'))
joblib.dump(selected_names, os.path.join(MODELS_DIR, 'selected_feature_names.pkl'))
joblib.dump(vectorizer_full, os.path.join(MODELS_DIR, 'tfidf_vectorizer_full.pkl'))

print(f'Modèle sauvegardé         : {MODELS_DIR}best_selected_classifier.pkl')
print(f'Features sélectionnées    : {MODELS_DIR}selected_feature_names.pkl ({len(selected_names)})')
print(f'Vectorizer sauvegardé     : {MODELS_DIR}tfidf_vectorizer_full.pkl')"""),
    ]


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    base = 'notebooks/4-ML-classique'
    print('Génération des notebooks ML refactorisés...')
    save_nb(gen_01(), f'{base}/01-ml-tfidf.ipynb')
    save_nb(gen_02(), f'{base}/02-ml-ngram.ipynb')
    save_nb(gen_03(), f'{base}/03-ml-llm.ipynb')
    save_nb(gen_04(), f'{base}/04-selection-variables.ipynb')
    print('Done!')
