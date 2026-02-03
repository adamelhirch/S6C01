---
description: Configurer l'environnement de développement S6C01
---

# Setup Environnement S6C01

Ce workflow guide la configuration initiale de l'environnement pour le projet S6C01 (Analyse Yelp).

## Prérequis

- Python 3.12+ installé
- Git configuré
- Données Yelp téléchargées depuis le sujet

## Étapes

### 1. Vérifier Python

```bash
python3 --version
```

Résultat attendu: `Python 3.12.x` ou supérieur

### 2. Créer l'environnement virtuel

// turbo
```bash
cd "/Users/adamelhirch/Documents/BUT/Semestre 6/S6C01"
python3 -m venv venv
```

### 3. Activer l'environnement virtuel

// turbo
```bash
source venv/bin/activate
```

Sur Windows:
```bash
venv\Scripts\activate
```

### 4. Mettre à jour pip

// turbo
```bash
pip install --upgrade pip
```

### 5. Installer les dépendances

// turbo
```bash
pip install -r requirements.txt
```

Cette étape peut prendre plusieurs minutes (Transformers, PyTorch, etc.)

### 6. Télécharger les ressources NLTK

// turbo
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab')"
```

### 7. Vérifier la structure des données

```bash
ls -lh data/raw/
```

Vous devriez voir:
- `yelp_academic_dataset_business.json` (~120 MB)
- `yelp_academic_reviews4students.jsonl` (~5 GB)
- `yelp_academic_dataset_user4students.jsonl` (~600 MB)

⚠️ **Si les fichiers sont manquants**, téléchargez-les depuis le sujet et placez-les dans `data/raw/`

### 8. Vérifier l'installation

// turbo
```bash
python -c "import pandas as pd; import numpy as np; import nltk; import transformers; print('✅ Tout est OK!')"
```

## Résultat attendu

- ✅ Environnement virtuel créé et activé
- ✅ Toutes les dépendances installées
- ✅ Ressources NLTK téléchargées
- ✅ Données Yelp présentes dans `data/raw/`

## Prochaines étapes

Utilisez le workflow `/start-development` pour commencer à travailler sur une story Linear.
