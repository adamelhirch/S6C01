---
description: Configurer l'environnement de développement S6C01
---

# Setup Environnement S6C01

Configuration initiale de l'environnement pour le projet.

## Prérequis

- Python 3.12+ installé
- Git configuré
- Données Yelp téléchargées depuis le sujet

## Étapes

### 1. Vérifier Python

```bash
python3 --version
```

### 2. Créer l'environnement virtuel

```bash
cd "/Users/adamelhirch/Documents/BUT/Semestre 6/S6C01"
python3 -m venv venv
```

### 3. Activer le venv

```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Télécharger les ressources NLTK

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab')"
```

### 6. Vérifier les données

```bash
ls -lh data/raw/
```

Fichiers attendus :
- `yelp_academic_dataset_business.json` (~120 MB)
- `yelp_academic_reviews4students.jsonl` (~5 GB)
- `yelp_academic_dataset_user4students.jsonl` (~600 MB)

### 7. Vérifier l'installation

```bash
python -c "import pandas as pd; import numpy as np; import nltk; import transformers; print('Tout est OK!')"
```

## Résultat attendu

- ✅ Venv créé et activé
- ✅ Dépendances installées
- ✅ Ressources NLTK téléchargées
- ✅ Données Yelp dans `data/raw/`
