# Guide Jupyter - Travailler avec les notebooks

**Pour utilisateurs claude-cli et développement manuel**

## Vue d'ensemble

Ce guide explique comment lancer Jupyter, créer des notebooks et suivre les bonnes pratiques du projet.

## Prérequis

- Environnement virtuel configuré (voir `WORKFLOW_SETUP.md`)
- Dépendances installées

## Lancer Jupyter

### 1. Activer l'environnement virtuel

**macOS/Linux:**
```bash
cd "/chemin/vers/S6C01"
source venv/bin/activate
```

**Windows:**
```cmd
cd "C:\chemin\vers\S6C01"
venv\Scripts\activate
```

### 2. Lancer Jupyter Notebook

```bash
jupyter notebook
```

**OU** Jupyter Lab (interface plus moderne):
```bash
jupyter lab
```

Jupyter s'ouvrira automatiquement dans votre navigateur à:
```
http://localhost:8888
```

### 3. Naviguer vers les notebooks

Dans l'interface Jupyter, ouvrez le dossier `notebooks/`

## Organisation des notebooks

Les notebooks sont numérotés par ordre d'exécution:

- `01-10`: Data loading et cleaning
- `11-20`: EDA (Exploratory Data Analysis)
- `21-30`: Feature engineering
- `31-40`: Modèles ML classiques
- `41-50`: Deep Learning / LLM
- `51+`: Expérimentations avancées

**Exemples:**
- `01_data_loading.ipynb`
- `05_tfidf_vectorization.ipynb`
- `12_sentiment_analysis.ipynb`

## Créer un nouveau notebook

### 1. Nomenclature

Format: `XX_description.ipynb`

Exemples:
- `05_tfidf_analysis.ipynb`
- `12_word_embeddings.ipynb`
- `35_bert_classification.ipynb`

### 2. Template de base

**Première cellule (Header):**
```python
"""
Epic X - Story SAE-XX - [Titre de la story]
Auteur: [Prénom NOM]
Date: [YYYY-MM-DD]
Description: [Objectif du notebook]
"""
```

**Deuxième cellule (Imports):**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# Configuration affichage
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Style visualisations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
```

**Troisième cellule (Load Data):**
```python
# Charger les données nettoyées (rapide avec Parquet)
df_reviews = pd.read_parquet('data/cleaned/reviews_clean.parquet')
print(f"Loaded {len(df_reviews):,} reviews")
df_reviews.head()
```

## Bonnes pratiques

### Structure recommandée

1. **Header** + Imports
2. **Chargement des données**
3. **Exploration** (`.head()`, `.info()`, `.describe()`)
4. **Preprocessing / Transformation**
5. **Analyse / Visualisation / Modélisation**
6. **Export des résultats**
7. **Conclusion** (cellule markdown)

### Avant de commiter

**IMPORTANT:** Toujours nettoyer les outputs avant de commiter:

1. Dans Jupyter: `Cell → All Output → Clear`
2. Sauvegarder: `Ctrl+S` (ou `Cmd+S` sur Mac)
3. Commiter le notebook

**Pourquoi?** Les outputs peuvent être volumineux et polluent l'historique Git.

### Exécution des cellules

- **Exécuter une cellule:** `Shift+Enter`
- **Exécuter toutes les cellules:** `Cell → Run All`
- **Redémarrer le kernel:** `Kernel → Restart`
- **Redémarrer et tout exécuter:** `Kernel → Restart & Run All`

## Charger les données nettoyées

Dans tous vos notebooks, utilisez Parquet (pas JSON):

```python
import pandas as pd

# Charger les données nettoyées (RAPIDE)
df_business = pd.read_parquet('data/cleaned/business_clean.parquet')
df_reviews = pd.read_parquet('data/cleaned/reviews_clean.parquet')
df_users = pd.read_parquet('data/cleaned/users_clean.parquet')

print(f"Business: {len(df_business):,} rows")
print(f"Reviews: {len(df_reviews):,} rows")
print(f"Users: {len(df_users):,} rows")
```

## Gestion de la mémoire

Pour les gros datasets:

```python
# Charger seulement les colonnes nécessaires
df = pd.read_parquet('data/cleaned/reviews_clean.parquet',
                     columns=['review_id', 'text_clean', 'stars'])

# Sampler si nécessaire (pour tests rapides)
df_sample = df.sample(n=100000, random_state=42)
```

## Visualisations

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Créer une figure avec plusieurs plots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Histogram
axes[0].hist(df['stars'], bins=5, color='skyblue', edgecolor='black')
axes[0].set_title('Distribution des notes')
axes[0].set_xlabel('Stars')
axes[0].set_ylabel('Fréquence')

# Plot 2: Bar chart
top_cities = df['city'].value_counts().head(10)
top_cities.plot(kind='barh', ax=axes[1], color='coral')
axes[1].set_title('Top 10 villes')

plt.tight_layout()

# Sauvegarder
plt.savefig('outputs/figures/distribution_stars.png', dpi=300, bbox_inches='tight')
plt.show()
```

## Arrêter Jupyter

Dans le terminal où Jupyter est lancé:
- Appuyer sur `Ctrl+C` deux fois
- Confirmer avec `y`

## Tips et astuces

### Kernel freeze
Si un notebook ne répond plus:
- `Kernel → Interrupt`
- Si ça ne marche pas: `Kernel → Restart`

### Auto-save
Jupyter sauvegarde automatiquement toutes les 2 minutes, mais prenez l'habitude de sauvegarder manuellement (`Ctrl+S`).

### Extensions utiles
Pour améliorer l'interface Jupyter:
```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

### Progress bars
Pour les opérations longues, utilisez tqdm:
```python
from tqdm import tqdm
tqdm.pandas(desc="Processing")

df['text_clean'] = df['text'].progress_apply(preprocess_text)
```

## Checklist avant commit

- [ ] Tous les outputs nettoyés (`Cell → All Output → Clear`)
- [ ] Notebook s'exécute sans erreurs (`Kernel → Restart & Run All`)
- [ ] Nomenclature correcte (`XX_description.ipynb`)
- [ ] Header présent avec Epic/Story/Auteur/Date
- [ ] Chemins relatifs (pas de chemins absolus hardcodés)
- [ ] Sauvegardé (`Ctrl+S`)

## Problèmes courants

### "Kernel not found"
**Solution:** Réinstallez le kernel ipython:
```bash
pip install ipykernel
python -m ipykernel install --user
```

### Import errors dans le notebook
**Solution:** Vérifiez que le venv est activé AVANT de lancer jupyter

### Notebook ne se sauvegarde pas
**Solution:** Vérifiez les permissions du fichier et du dossier

## Ressources

- [Jupyter Documentation](https://jupyter-notebook.readthedocs.io/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/)

## Prochaines étapes

- `WORKFLOW_DEVELOPMENT.md` - Pour le workflow Git complet
- `WORKFLOW_DATA_PIPELINE.md` - Pour comprendre le pipeline de données
- `AI_INSTRUCTIONS.md` - Pour plus de patterns et bonnes pratiques
