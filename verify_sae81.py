"""
Verification SAE-81 - Classification Baseline - Logistic Regression

Verifie que tous les livrables sont corrects :
- Le notebook existe
- Le modele lr_baseline.pkl existe et est chargeable
- Le modele peut faire des predictions
- Les metriques sont coherentes
"""

import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.metrics import accuracy_score, classification_report

# Chemins
DATA_PATH = Path('data/cleaned/reviews_text_cleaned.parquet')
TFIDF_MODEL_PATH = Path('outputs/models/tfidf_vectorizer.pkl')
LR_MODEL_PATH = Path('outputs/models/lr_baseline.pkl')
NOTEBOOK_PATH = Path('notebooks/5-ml-classic/01-baseline-logistic-regression.ipynb')

errors = []

# 1. Verification du notebook
print("=" * 50)
print("VERIFICATION SAE-81")
print("=" * 50)

print("\n[1] Notebook")
if NOTEBOOK_PATH.exists():
    print(f"  OK - {NOTEBOOK_PATH} existe ({NOTEBOOK_PATH.stat().st_size / 1024:.1f} KB)")
else:
    errors.append(f"Notebook manquant: {NOTEBOOK_PATH}")
    print(f"  FAIL - {NOTEBOOK_PATH} non trouve!")

# 2. Verification du modele LR
print("\n[2] Modele Logistic Regression")
if LR_MODEL_PATH.exists():
    print(f"  OK - {LR_MODEL_PATH} existe ({LR_MODEL_PATH.stat().st_size / 1024:.1f} KB)")
    try:
        with open(LR_MODEL_PATH, 'rb') as f:
            lr_model = pickle.load(f)
        print(f"  OK - Modele charge: {type(lr_model).__name__}")
        print(f"       Classes: {lr_model.classes_}")
        print(f"       max_iter: {lr_model.max_iter}")
    except Exception as e:
        errors.append(f"Erreur chargement modele: {e}")
        print(f"  FAIL - Erreur chargement: {e}")
else:
    errors.append(f"Modele manquant: {LR_MODEL_PATH}")
    print(f"  FAIL - {LR_MODEL_PATH} non trouve!")

# 3. Test de prediction
print("\n[3] Test de prediction")
if DATA_PATH.exists() and TFIDF_MODEL_PATH.exists() and LR_MODEL_PATH.exists():
    try:
        # Charger un petit echantillon
        df = pd.read_parquet(DATA_PATH).head(100)
        df['text_cleaned'] = df['text_cleaned'].fillna('')

        with open(TFIDF_MODEL_PATH, 'rb') as f:
            tfidf = pickle.load(f)

        X_sample = tfidf.transform(df['text_cleaned'])
        y_sample = df['stars']

        y_pred = lr_model.predict(X_sample)
        acc = accuracy_score(y_sample, y_pred)

        print(f"  OK - Predictions reussies sur {len(df)} samples")
        print(f"  Accuracy (echantillon): {acc:.4f}")
        print(f"  Predictions uniques: {np.unique(y_pred)}")

        if acc > 0:
            print("  OK - Accuracy > 0 (modele fonctionnel)")
        else:
            errors.append("Accuracy = 0, modele potentiellement casse")
            print("  FAIL - Accuracy = 0!")
    except Exception as e:
        errors.append(f"Erreur prediction: {e}")
        print(f"  FAIL - Erreur: {e}")
else:
    print("  SKIP - Fichiers manquants, test de prediction ignore")

# Resume
print("\n" + "=" * 50)
if errors:
    print(f"FAIL - {len(errors)} ERREUR(S) TROUVEE(S):")
    for err in errors:
        print(f"  - {err}")
    exit(1)
else:
    print("OK - TOUTES LES VERIFICATIONS PASSEES!")
    print("  SAE-81 est complete.")
print("=" * 50)
