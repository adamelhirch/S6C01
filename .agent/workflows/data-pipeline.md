---
description: Pipeline de chargement et nettoyage des données Yelp
---

# Pipeline de Données Yelp

Ce workflow explique le pipeline de traitement des données Yelp depuis les fichiers JSON bruts jusqu'aux fichiers Parquet nettoyés.

## Architecture du Pipeline

```
data/raw/*.json → Chargement → Nettoyage → data/cleaned/*.parquet
```

## Fichiers de Données

### Inputs (data/raw/)

1. **yelp_academic_dataset_business.json** (~120 MB)
   - ~150k commerces (restaurants, bars, hôtels)
   - Colonnes: business_id, name, address, city, state, stars, review_count, categories, etc.

2. **yelp_academic_reviews4students.jsonl** (~5 GB)
   - ~6M avis textuels
   - Colonnes: review_id, user_id, business_id, stars, text, date, etc.

3. **yelp_academic_dataset_user4students.jsonl** (~600 MB)
   - ~2M profils utilisateurs
   - Colonnes: user_id, name, review_count, average_stars, friends, etc.

### Outputs (data/cleaned/)

- `business_clean.parquet`
- `reviews_clean.parquet`
- `users_clean.parquet`

⚠️ **Format Parquet**: Plus rapide et plus compact que JSON/CSV

## Étapes du Pipeline

### 1. Chargement des données brutes

**Notebook**: `notebooks/01_data_loading.ipynb`

**Code Python** (dans le notebook):
```python
import pandas as pd
import json

# Charger business (JSON standard)
with open('data/raw/yelp_academic_dataset_business.json', 'r') as f:
    business_data = [json.loads(line) for line in f]
df_business = pd.DataFrame(business_data)

# Charger reviews (JSONL - une ligne par JSON)
df_reviews = pd.read_json('data/raw/yelp_academic_reviews4students.jsonl', lines=True)

# Charger users (JSONL)
df_users = pd.read_json('data/raw/yelp_academic_dataset_user4students.jsonl', lines=True)

print(f"Business: {len(df_business)} rows")
print(f"Reviews: {len(df_reviews)} rows")
print(f"Users: {len(df_users)} rows")
```

### 2. Nettoyage des données

**Notebook**: `notebooks/02_data_cleaning.ipynb`

**Opérations de nettoyage**:

1. **Supprimer les doublons**
```python
df_business = df_business.drop_duplicates(subset=['business_id'])
df_reviews = df_reviews.drop_duplicates(subset=['review_id'])
df_users = df_users.drop_duplicates(subset=['user_id'])
```

2. **Gérer les valeurs manquantes**
```python
# Remplir ou supprimer les NaN selon les colonnes
df_business['categories'] = df_business['categories'].fillna('')
df_reviews = df_reviews.dropna(subset=['text', 'stars'])
```

3. **Nettoyer les textes (reviews)**
```python
import re

def clean_text(text):
    # Minuscules
    text = text.lower()
    # Retirer URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # Retirer caractères spéciaux (garder lettres, chiffres, espaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Normaliser espaces
    text = ' '.join(text.split())
    return text

df_reviews['text_clean'] = df_reviews['text'].apply(clean_text)
```

4. **Convertir les types de données**
```python
df_reviews['date'] = pd.to_datetime(df_reviews['date'])
df_reviews['stars'] = df_reviews['stars'].astype(int)
```

### 3. Export en Parquet

**Notebook**: `notebooks/02_data_cleaning.ipynb` (fin)

```python
# Créer le dossier si nécessaire
import os
os.makedirs('data/cleaned', exist_ok=True)

# Sauvegarder en Parquet
df_business.to_parquet('data/cleaned/business_clean.parquet', index=False)
df_reviews.to_parquet('data/cleaned/reviews_clean.parquet', index=False)
df_users.to_parquet('data/cleaned/users_clean.parquet', index=False)

print("✅ Données nettoyées sauvegardées en Parquet")
```

### 4. Charger les données nettoyées (notebooks suivants)

**Dans tous les notebooks suivants**:
```python
import pandas as pd

# Charger depuis Parquet (RAPIDE)
df_business = pd.read_parquet('data/cleaned/business_clean.parquet')
df_reviews = pd.read_parquet('data/cleaned/reviews_clean.parquet')
df_users = pd.read_parquet('data/cleaned/users_clean.parquet')

print(f"Business: {len(df_business)} rows")
print(f"Reviews: {len(df_reviews)} rows")
print(f"Users: {len(df_users)} rows")
```

## Résultat attendu

- ✅ Données chargées depuis `data/raw/`
- ✅ Nettoyage effectué (doublons, NaN, texte)
- ✅ Données sauvegardées dans `data/cleaned/*.parquet`
- ✅ Chargement ultra-rapide avec `pd.read_parquet()`

## Structure des DataFrames nettoyés

### business_clean.parquet
- `business_id` (str) - ID unique
- `name` (str) - Nom du commerce
- `city`, `state` (str) - Localisation
- `stars` (float) - Note moyenne (1.0 à 5.0)
- `review_count` (int) - Nombre d'avis
- `categories` (str) - Catégories séparées par virgules

### reviews_clean.parquet
- `review_id` (str) - ID unique
- `business_id` (str) - ID du commerce
- `user_id` (str) - ID utilisateur
- `stars` (int) - Note (1 à 5)
- `text` (str) - Texte original
- `text_clean` (str) - Texte nettoyé
- `date` (datetime) - Date de l'avis

### users_clean.parquet
- `user_id` (str) - ID unique
- `name` (str) - Nom utilisateur
- `review_count` (int) - Nombre d'avis écrits
- `average_stars` (float) - Note moyenne donnée

## Workflows connexes

- `/setup-environment` - Configuration initiale
- `/run-jupyter` - Lancer Jupyter pour exécuter les notebooks
