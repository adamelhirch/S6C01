# 🤖 Instructions pour Assistants IA

Ce document fournit des instructions spécifiques pour les assistants IA (Antigravity, Claude, etc.) travaillant sur le projet S6C01.

---

## 📚 Comment interpréter la structure du projet

### Organisation logique

Le projet suit une organisation **Data Science classique**:

```
Code exploratoire → Code réutilisable → Outputs
  (notebooks/)         (src/)          (outputs/)
```

**Notebooks** (`notebooks/`)
- Exploration interactive et prototypage
- Nomenclature: `XX_description.ipynb` (ordre d'exécution)
- Cellules exécutables une par une
- **Usage**: Découverte, visualisation, expérimentation

**Code source** (`src/`)
- Fonctions et classes réutilisables
- Code testé et documenté
- **Usage**: Appelé depuis les notebooks ou d'autres scripts

**Outputs** (`outputs/`)
- Résultats finaux: graphiques, rapports, modèles
- **Usage**: Artefacts générés par notebooks/scripts

### Flux de données

```
1. data/raw/*.json           → Données brutes (NON versionnées)
2. notebooks/01_*.ipynb      → Chargement
3. data/cleaned/*.parquet    → Données nettoyées (NON versionnées)
4. notebooks/0X_*.ipynb      → Analyse / ML
5. outputs/figures/          → Visualisations finales
```

---

## 🎯 Conventions de Code

### Notebooks Jupyter

**Header de notebook** (première cellule):
```python
"""
Epic X - Story SAE-XX - Titre de la story
Auteur: Prénom NOM
Date: YYYY-MM-DD
Description: Brève description de l'objectif du notebook
"""

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

**Sections recommandées**:
1. Header + Imports
2. Chargement des données
3. Exploration (`.head()`, `.info()`, `.describe()`)
4. Preprocessing / Transformation
5. Analyse / Visualisation / Modélisation
6. Export des résultats
7. Conclusion (markdown cell)

**Avant de commiter**:
- `Cell → All Output → Clear` (nettoyer les outputs)
- Vérifier qu'il n'y a pas d'erreurs à la ré-exécution

### Code Python (src/)

**Structure d'un fichier**:
```python
"""
Module description

This module provides utilities for [purpose].
"""

import pandas as pd
from typing import List, Dict, Optional

# Constants
DEFAULT_ENCODING = 'utf-8'


def function_name(param1: str, param2: int = 10) -> pd.DataFrame:
    """
    Brief description.
    
    Args:
        param1: Description of param1
        param2: Description of param2 (default: 10)
    
    Returns:
        Description of return value
    
    Example:
        >>> result = function_name("test", 5)
    """
    # Implementation
    pass
```

**Style**:
- PEP 8 (conformité Python standard)
- Type hints pour toutes les fonctions
- Docstrings Google-style
- Snake_case pour variables et fonctions
- PascalCase pour classes

---

## 🔄 Patterns Courants

### Charger des données nettoyées

```python
import pandas as pd

# TOUJOURS utiliser Parquet (rapide et compact)
df_business = pd.read_parquet('data/cleaned/business_clean.parquet')
df_reviews = pd.read_parquet('data/cleaned/reviews_clean.parquet')
df_users = pd.read_parquet('data/cleaned/users_clean.parquet')

print(f"Loaded {len(df_reviews):,} reviews")
```

### Preprocessing NLP

```python
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Stopwords anglais
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text: str) -> str:
    """Nettoie et normalise un texte."""
    # Lowercase
    text = text.lower()
    
    # Remove URLs, emails
    text = re.sub(r'http\S+|www\S+|[\w\.-]+@[\w\.-]+', '', text)
    
    # Keep only letters, numbers, spaces
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords and lemmatize
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    
    return ' '.join(tokens)

# Appliquer avec progress bar
from tqdm import tqdm
tqdm.pandas(desc="Preprocessing")
df['text_clean'] = df['text'].progress_apply(preprocess_text)
```

### Visualisations

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Créer une figure
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1
axes[0].hist(df['stars'], bins=5, color='skyblue', edgecolor='black')
axes[0].set_title('Distribution des notes')
axes[0].set_xlabel('Stars')
axes[0].set_ylabel('Fréquence')

# Plot 2
top_cities = df['city'].value_counts().head(10)
top_cities.plot(kind='barh', ax=axes[1], color='coral')
axes[1].set_title('Top 10 villes')

plt.tight_layout()

# Sauvegarder
plt.savefig('outputs/figures/distribution_stars.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## ✨ Comment créer de nouveaux notebooks

### Nomenclature

**Format**: `XX_description.ipynb`

Numéros suggérés:
- `01-10`: Data loading et cleaning
- `11-20`: EDA (Exploratory Data Analysis)
- `21-30`: Feature engineering
- `31-40`: Modèles ML classiques
- `41-50`: Deep Learning / LLM
- `51+`: Expérimentations avancées

**Exemples**:
- `05_tfidf_vectorization.ipynb`
- `12_sentiment_analysis.ipynb`
- `35_recommendation_system.ipynb`
- `42_bert_fine_tuning.ipynb`

### Template de nouveau notebook

```python
# === CELL 1: Header ===
"""
Epic X - Story SAE-XX - [Titre de la story]
Auteur: [Prénom NOM]
Date: [YYYY-MM-DD]
Description: [Objectif du notebook]
"""

# === CELL 2: Imports ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# Configuration
pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8-darkgrid')

# === CELL 3: Load Data ===
df = pd.read_parquet('data/cleaned/reviews_clean.parquet')
print(f"Loaded {len(df):,} reviews")
df.head()

# === CELLS 4+: Analysis ===
# [Votre code d'analyse]

# === LAST CELL: Conclusion ===
# [Markdown cell avec résumé des findings]
```

---

## 📝 Comment documenter le code

### Commentaires dans notebooks

**Bon**:
```python
# Calculate TF-IDF for top 1000 features
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X = tfidf_vectorizer.fit_transform(df['text_clean'])
```

**Mauvais** (trop verbeux):
```python
# First we create a TfidfVectorizer object with 1000 max features
# Then we fit it on the cleaned text column
# Then we transform the text into a matrix
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X = tfidf_vectorizer.fit_transform(df['text_clean'])
```

### Markdown cells

Utiliser des markdown cells pour:
- Introduire chaque section
- Expliquer le raisonnement
- Résumer les résultats

**Exemple**:
```markdown
## 3. Sentiment Analysis

We'll use TextBlob to compute sentiment polarity for each review.
Polarity ranges from -1 (negative) to +1 (positive).

**Hypothesis**: Higher star ratings should correlate with positive sentiment.
```

### Docstrings pour fonctions (src/)

```python
def load_and_merge_data(
    business_path: str,
    reviews_path: str,
    sample_size: Optional[int] = None
) -> pd.DataFrame:
    """
    Load and merge business and reviews data.
    
    This function loads business and reviews Parquet files, merges them
    on business_id, and optionally samples the result.
    
    Args:
        business_path: Path to business Parquet file
        reviews_path: Path to reviews Parquet file
        sample_size: Number of rows to sample (None = all rows)
    
    Returns:
        Merged DataFrame with business and review information
    
    Raises:
        FileNotFoundError: If input files don't exist
    
    Example:
        >>> df = load_and_merge_data(
        ...     'data/cleaned/business_clean.parquet',
        ...     'data/cleaned/reviews_clean.parquet',
        ...     sample_size=10000
        ... )
        >>> print(len(df))
        10000
    """
    # Implementation
```

---

## 🚨 Pièges à éviter

### ❌ Ne JAMAIS faire

1. **Commiter les outputs de notebooks**
   - Toujours `Cell → All Output → Clear` avant commit
   - Raison: Outputs volumineux, pollue Git

2. **Commiter les données brutes/nettoyées**
   - `data/raw/` et `data/cleaned/` sont dans `.gitignore`
   - Raison: Fichiers trop gros (~6 GB)

3. **Hardcoder des chemins absolus**
   ```python
   # ❌ Mauvais
   df = pd.read_csv('/Users/adam/Documents/S6C01/data/...')
   
   # ✅ Bon
   df = pd.read_parquet('data/cleaned/reviews_clean.parquet')
   ```

4. **Oublier d'activer le venv**
   - Toujours `source venv/bin/activate` avant de travailler
   - Vérifier: `which python` doit pointer vers `venv/bin/python`

5. **Travailler directement sur `main`**
   - TOUJOURS créer une branche: `git checkout -b prenom/sae-XX-description`

### ⚠️ Faire attention

1. **Gestion mémoire avec gros datasets**
   ```python
   # Charger seulement les colonnes nécessaires
   df = pd.read_parquet('data/cleaned/reviews_clean.parquet',
                        columns=['review_id', 'text_clean', 'stars'])
   
   # Sampler si nécessaire
   df_sample = df.sample(n=100000, random_state=42)
   ```

2. **Encodage des textes**
   - Toujours utiliser `encoding='utf-8'` pour les fichiers texte
   - Yelp reviews contiennent des caractères spéciaux

3. **Random seeds pour reproductibilité**
   ```python
   import random
   import numpy as np
   
   random.seed(42)
   np.random.seed(42)
   ```

---

## 💡 Suggestions pour assister efficacement

### Quand un utilisateur demande de l'aide

1. **Identifier le contexte**:
   - Quelle Epic/Story (SAE-XX) ?
   - Quel fichier/notebook ?
   - Quel est l'objectif final ?

2. **Vérifier la structure**:
   - Exploration → `notebooks/`
   - Code réutilisable → `src/`
   - Résultats → `outputs/`

3. **Proposer du code robuste**:
   - Gestion d'erreurs avec try/except
   - Progress bars pour opérations longues
   - Commentaires clairs et concis

4. **Respecter les conventions**:
   - Nomenclature des fichiers
   - Format des commits (SAE-XX)
   - Type hints et docstrings

5. **Être pédagogique**:
   - Expliquer les choix techniques
   - Suggérer des alternatives
   - Pointer vers la documentation

### Exemples de réponses optimales

**Question**: "Comment charger les reviews Yelp ?"

**Réponse IA**:
```python
# Charger les reviews nettoyées (Parquet = rapide)
import pandas as pd

df_reviews = pd.read_parquet('data/cleaned/reviews_clean.parquet')
print(f"Loaded {len(df_reviews):,} reviews")
print(f"Columns: {df_reviews.columns.tolist()}")
df_reviews.head()

# Si besoin de sampler (pour tester rapidement)
df_sample = df_reviews.sample(n=10000, random_state=42)
```

**Explications** :
- Utilise Parquet (format optimisé déjà nettoyé)
- Affiche des infos utiles (nombre de rows, colonnes)
- Suggère un sampling pour tests rapides

---

## 📚 Ressources recommandées

- **Pandas**: https://pandas.pydata.org/docs/user_guide/index.html
- **Scikit-learn**: https://scikit-learn.org/stable/user_guide.html
- **NLTK**: https://www.nltk.org/book/
- **Matplotlib**: https://matplotlib.org/stable/tutorials/index.html
- **HuggingFace**: https://huggingface.co/docs/transformers/index

---

**Dernière mise à jour**: 2026-02-03
