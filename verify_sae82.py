"""
Verification SAE-82 - Comparaison Modeles ML (SVM, RF, NB)

Verifie:
- Le notebook existe
- Le CSV comparatif existe et contient 4 modeles
- Le meilleur modele existe et est chargeable
"""

import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.metrics import accuracy_score

NOTEBOOK_PATH = Path('notebooks/5-ml-classic/02-model-comparison.ipynb')
CSV_PATH = Path('outputs/ml_models_comparison.csv')
BEST_MODEL_PATH = Path('outputs/models/best_ml_model.pkl')
TFIDF_MODEL_PATH = Path('outputs/models/tfidf_vectorizer.pkl')
DATA_PATH = Path('data/cleaned/reviews_text_cleaned.parquet')

errors = []

print("=" * 50)
print("VERIFICATION SAE-82")
print("=" * 50)

# 1. Notebook
print("\n[1] Notebook")
if NOTEBOOK_PATH.exists():
    print(f"  OK - {NOTEBOOK_PATH} ({NOTEBOOK_PATH.stat().st_size / 1024:.1f} KB)")
else:
    errors.append("Notebook manquant")
    print(f"  FAIL - {NOTEBOOK_PATH}")

# 2. CSV comparatif
print("\n[2] CSV comparatif")
if CSV_PATH.exists():
    csv_df = pd.read_csv(CSV_PATH)
    print(f"  OK - {CSV_PATH} ({len(csv_df)} modeles)")
    print(csv_df.to_string(index=False))
    if len(csv_df) < 4:
        errors.append(f"CSV ne contient que {len(csv_df)} modeles (attendu 4)")
        print(f"  FAIL - Seulement {len(csv_df)} modeles")
    else:
        print(f"  OK - 4 modeles presents")
else:
    errors.append("CSV manquant")
    print(f"  FAIL - {CSV_PATH}")

# 3. Meilleur modele
print("\n[3] Meilleur modele")
if BEST_MODEL_PATH.exists():
    try:
        with open(BEST_MODEL_PATH, 'rb') as f:
            best_model = pickle.load(f)
        print(f"  OK - {type(best_model).__name__} charge ({BEST_MODEL_PATH.stat().st_size / 1024:.1f} KB)")

        # Test prediction
        if DATA_PATH.exists() and TFIDF_MODEL_PATH.exists():
            df = pd.read_parquet(DATA_PATH).head(50)
            df['text_cleaned'] = df['text_cleaned'].fillna('')
            with open(TFIDF_MODEL_PATH, 'rb') as f:
                tfidf = pickle.load(f)
            X_sample = tfidf.transform(df['text_cleaned'])
            y_pred = best_model.predict(X_sample)
            acc = accuracy_score(df['stars'], y_pred)
            print(f"  OK - Prediction test: accuracy={acc:.4f}")
    except Exception as e:
        errors.append(f"Erreur modele: {e}")
        print(f"  FAIL - {e}")
else:
    errors.append("Meilleur modele manquant")
    print(f"  FAIL - {BEST_MODEL_PATH}")

# Resume
print("\n" + "=" * 50)
if errors:
    print(f"FAIL - {len(errors)} erreur(s):")
    for e in errors:
        print(f"  - {e}")
    exit(1)
else:
    print("OK - TOUTES LES VERIFICATIONS PASSEES!")
    print("  SAE-82 est complete.")
print("=" * 50)
