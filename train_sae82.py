"""Train and compare ML models for SAE-82 - optimized version."""
import pandas as pd
import numpy as np
import pickle
import time
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    classification_report, accuracy_score,
    precision_score, recall_score, f1_score
)
import warnings
warnings.filterwarnings('ignore')

# Force flush prints immediately
def log(msg):
    print(msg)
    sys.stdout.flush()

DATA_PATH = Path('data/cleaned/reviews_text_cleaned.parquet')
TFIDF_MODEL_PATH = Path('outputs/models/tfidf_vectorizer.pkl')
OUTPUT_CSV = Path('outputs/ml_models_comparison.csv')
BEST_MODEL_PATH = Path('outputs/models/best_ml_model.pkl')

# Load data
log("Loading data...")
df = pd.read_parquet(DATA_PATH)
df['text_cleaned'] = df['text_cleaned'].fillna('')
log(f"  {len(df):,} reviews")

# Load TF-IDF
log("Loading TF-IDF...")
with open(TFIDF_MODEL_PATH, 'rb') as f:
    tfidf = pickle.load(f)
log(f"  {len(tfidf.vocabulary_):,} terms")

# Transform & split
log("Transforming...")
X = tfidf.transform(df['text_cleaned'])
y = df['stars']
log(f"  X shape: {X.shape}")

log("Splitting...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
log(f"  Train: {X_train.shape[0]:,} | Test: {X_test.shape[0]:,}")

# Models - RF reduced to 50 estimators for speed
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42, solver='lbfgs'),
    'LinearSVC (SVM)': LinearSVC(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1),
    'Naive Bayes': MultinomialNB()
}

results = []

for name, model in models.items():
    log(f"\n=== {name} ===")
    start = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - start
    log(f"  Trained in {train_time:.2f}s")

    log("  Predicting...")
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted')
    rec = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    results.append({
        'Model': name,
        'Accuracy': round(acc, 4),
        'Precision': round(prec, 4),
        'Recall': round(rec, 4),
        'F1': round(f1, 4),
        'Train Time (s)': round(train_time, 2)
    })

    log(f"  Accuracy: {acc:.4f} | F1: {f1:.4f}")
    log(classification_report(y_test, y_pred))

# Results table
results_df = pd.DataFrame(results).sort_values('F1', ascending=False)
log("\n=== TABLEAU COMPARATIF ===")
log(results_df.to_string(index=False))

# Save CSV
OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
results_df.to_csv(OUTPUT_CSV, index=False)
log(f"\nCSV saved: {OUTPUT_CSV}")

# Save best model
best_name = results_df.iloc[0]['Model']
best_model = models[best_name]
BEST_MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
with open(BEST_MODEL_PATH, 'wb') as f:
    pickle.dump(best_model, f)
log(f"Best model ({best_name}) saved: {BEST_MODEL_PATH}")
log("Done!")
