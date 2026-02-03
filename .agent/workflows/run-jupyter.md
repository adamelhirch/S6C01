---
description: Lancer Jupyter et travailler avec les notebooks
---

# Lancer Jupyter Notebook

Ce workflow guide le lancement de Jupyter et la navigation dans les notebooks du projet.

## Prérequis

- Environnement virtuel créé (voir `/setup-environment`)
- Dépendances installées

## Étapes

### 1. Activer l'environnement virtuel

// turbo
```bash
cd "/Users/adamelhirch/Documents/BUT/Semestre 6/S6C01"
source venv/bin/activate
```

Sur Windows:
```bash
venv\Scripts\activate
```

### 2. Lancer Jupyter Notebook

// turbo
```bash
jupyter notebook
```

Jupyter s'ouvrira automatiquement dans votre navigateur à l'adresse:
```
http://localhost:8888
```

### 3. Naviguer vers les notebooks

Dans l'interface Jupyter, ouvrir le dossier `notebooks/`

Les notebooks sont organisés par ordre:
- `01_data_loading.ipynb` - Chargement des données JSON
- `02_data_cleaning.ipynb` - Nettoyage des données
- `03_preprocessing.ipynb` - Preprocessing NLP
- `04_eda_dashboards.ipynb` - Exploration et visualisations
- etc.

### 4. Travailler sur un notebook

1. Ouvrir un notebook existant ou créer un nouveau
2. Exécuter les cellules avec `Shift+Enter`
3. Sauvegarder régulièrement avec `Ctrl+S` (ou `Cmd+S` sur Mac)

### 5. Créer un nouveau notebook

**Nomenclature**: `XX_description.ipynb`

Exemples:
- `05_tfidf_analysis.ipynb`
- `06_word2vec_training.ipynb`
- `07_classification_models.ipynb`

**Première cellule** (toujours inclure):
```python
# Epic X - Story SAE-XX - Titre de la story
# Auteur: Prénom NOM
# Date: YYYY-MM-DD

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration affichage
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
plt.style.use('seaborn-v0_8-darkgrid')
```

### 6. Arrêter Jupyter

Dans le terminal où Jupyter est lancé:
- Appuyer sur `Ctrl+C` deux fois
- Ou fermer le terminal

## Résultat attendu

- ✅ Jupyter lancé et accessible dans le navigateur
- ✅ Notebooks visibles dans `notebooks/`
- ✅ Possibilité de créer et exécuter des notebooks

## Tips

- **Kernel restart**: Si un notebook freeze, `Kernel → Restart`
- **Clear outputs**: `Cell → All Output → Clear` avant de commiter
- **Auto-save**: Jupyter sauvegarde automatiquement toutes les 2 minutes
- **Extensions**: Installer `jupyter contrib nbextensions` pour améliorer l'interface

## Workflows connexes

- `/data-pipeline` - Pour charger et nettoyer les données
- `/start-development` - Pour workflow complet Git + Linear
