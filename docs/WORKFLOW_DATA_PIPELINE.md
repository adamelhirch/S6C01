# Guide Pipeline de Données Yelp

**Pour utilisateurs claude-cli et développement manuel**

## Vue d'ensemble

Ce guide explique le pipeline de traitement des données Yelp, du JSON brut aux fichiers Parquet nettoyés prêts pour l'analyse.

## Architecture du pipeline

```
data/raw/*.json
    ↓ Chargement
    ↓ Exploration
    ↓ Nettoyage
    ↓ Validation
data/cleaned/*.parquet
```

## Les fichiers de données

### Inputs (data/raw/)

**⚠️ Ces fichiers ne sont PAS versionnés sur Git**

1. **yelp_academic_dataset_business.json** (~120 MB)
   - ~150,000 commerces
   - Restaurants, bars, hôtels, etc.
   - Colonnes: business_id, name, address, city, stars, categories...

2. **yelp_academic_reviews4students.jsonl** (~5 GB)
   - ~6,000,000 avis textuels
   - Format: JSONL (une ligne = un JSON)
   - Colonnes: review_id, user_id, business_id, stars, text, date...

3. **yelp_academic_dataset_user4students.jsonl** (~600 MB)
   - ~2,000,000 profils utilisateurs
   - Colonnes: user_id, name, review_count, average_stars, friends...

### Outputs (data/cleaned/)

**Format Parquet** (rapide, compact, préserve les types):

- `business_clean.parquet`
- `reviews_clean.parquet`
- `users_clean.parquet`

## Étapes du pipeline

### Phase 1: Chargement des données brutes

**Notebook:** `notebooks/01_data_loading.ipynb`

**Objectif:** Charger les 3 fichiers JSON en DataFrames Pandas

**Code pour Business (JSON standard):**
```python
import pandas as pd
import json

# Charger business (JSON avec une ligne par objet)
with open('data/raw/yelp_academic_dataset_business.json', 'r', encoding='utf-8') as f:
    business_data = [json.loads(line) for line in f]

df_business = pd.DataFrame(business_data)
print(f"Business: {len(df_business):,} rows")
print(f"Columns: {df_business.columns.tolist()}")
df_business.head()
```

**Code pour Reviews et Users (JSONL):**
```python
# Charger reviews (JSONL - format optimisé)
df_reviews = pd.read_json(
    'data/raw/yelp_academic_reviews4students.jsonl',
    lines=True,
    encoding='utf-8'
)
print(f"Reviews: {len(df_reviews):,} rows")

# Charger users (JSONL)
df_users = pd.read_json(
    'data/raw/yelp_academic_dataset_user4students.jsonl',
    lines=True,
    encoding='utf-8'
)
print(f"Users: {len(df_users):,} rows")
```

**Exploration initiale:**
```python
# Pour chaque DataFrame
df_business.info()
df_business.describe()
df_business.head(10)

# Vérifier les valeurs manquantes
print(df_business.isnull().sum())
```

### Phase 2: Nettoyage des données

**Notebook:** `notebooks/02_data_cleaning.ipynb`

**Objectifs:**
1. Supprimer les doublons
2. Gérer les valeurs manquantes
3. Nettoyer les textes
4. Convertir les types de données
5. Valider la cohérence

#### Étape 2.1: Supprimer les doublons

```python
# Business
print(f"Business avant: {len(df_business)}")
df_business = df_business.drop_duplicates(subset=['business_id'])
print(f"Business après: {len(df_business)}")

# Reviews
print(f"Reviews avant: {len(df_reviews)}")
df_reviews = df_reviews.drop_duplicates(subset=['review_id'])
print(f"Reviews après: {len(df_reviews)}")

# Users
print(f"Users avant: {len(df_users)}")
df_users = df_users.drop_duplicates(subset=['user_id'])
print(f"Users après: {len(df_users)}")
```

#### Étape 2.2: Gérer les valeurs manquantes

```python
# Business: remplir les catégories vides
df_business['categories'] = df_business['categories'].fillna('')

# Business: remplir les attributs vides
df_business['attributes'] = df_business['attributes'].fillna('{}')

# Reviews: supprimer les lignes sans texte ou sans note
df_reviews = df_reviews.dropna(subset=['text', 'stars'])

# Users: garder toutes les lignes (les NaN sont acceptables)
```

#### Étape 2.3: Nettoyer les textes (reviews)

```python
import re

def clean_text(text):
    """Nettoie un texte d'avis."""
    if pd.isna(text):
        return ""

    # Minuscules
    text = text.lower()

    # Retirer URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Retirer emails
    text = re.sub(r'[\w\.-]+@[\w\.-]+', '', text)

    # Garder seulement lettres, chiffres, espaces
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # Normaliser les espaces multiples
    text = ' '.join(text.split())

    return text

# Appliquer avec progress bar
from tqdm import tqdm
tqdm.pandas(desc="Cleaning text")

df_reviews['text_clean'] = df_reviews['text'].progress_apply(clean_text)
```

#### Étape 2.4: Convertir les types de données

```python
# Reviews: convertir dates
df_reviews['date'] = pd.to_datetime(df_reviews['date'])

# Reviews: convertir stars en int
df_reviews['stars'] = df_reviews['stars'].astype(int)

# Business: convertir stars en float
df_business['stars'] = df_business['stars'].astype(float)

# Business: convertir review_count en int
df_business['review_count'] = df_business['review_count'].astype(int)
```

#### Étape 2.5: Validation

```python
# Vérifier les ranges valides
assert df_reviews['stars'].between(1, 5).all(), "Invalid star ratings"
assert df_business['stars'].between(1.0, 5.0).all(), "Invalid business ratings"

# Vérifier les IDs uniques
assert df_business['business_id'].is_unique, "Duplicate business IDs"
assert df_reviews['review_id'].is_unique, "Duplicate review IDs"
assert df_users['user_id'].is_unique, "Duplicate user IDs"

print("✅ Validation passed!")
```

### Phase 3: Export en Parquet

**Notebook:** `notebooks/02_data_cleaning.ipynb` (fin)

```python
import os

# Créer le dossier si nécessaire
os.makedirs('data/cleaned', exist_ok=True)

# Sauvegarder en Parquet
df_business.to_parquet('data/cleaned/business_clean.parquet', index=False)
df_reviews.to_parquet('data/cleaned/reviews_clean.parquet', index=False)
df_users.to_parquet('data/cleaned/users_clean.parquet', index=False)

print("✅ Données nettoyées sauvegardées!")

# Vérifier la taille des fichiers
import os
for file in ['business_clean.parquet', 'reviews_clean.parquet', 'users_clean.parquet']:
    path = f'data/cleaned/{file}'
    size_mb = os.path.getsize(path) / (1024 * 1024)
    print(f"{file}: {size_mb:.2f} MB")
```

### Phase 4: Chargement rapide (notebooks suivants)

**Dans tous les notebooks suivants:**

```python
import pandas as pd

# Charger depuis Parquet (ULTRA RAPIDE - quelques secondes)
df_business = pd.read_parquet('data/cleaned/business_clean.parquet')
df_reviews = pd.read_parquet('data/cleaned/reviews_clean.parquet')
df_users = pd.read_parquet('data/cleaned/users_clean.parquet')

print(f"✅ Loaded {len(df_business):,} businesses")
print(f"✅ Loaded {len(df_reviews):,} reviews")
print(f"✅ Loaded {len(df_users):,} users")
```

**Charger seulement certaines colonnes (économise mémoire):**

```python
# Charger seulement les colonnes nécessaires
df_reviews = pd.read_parquet(
    'data/cleaned/reviews_clean.parquet',
    columns=['review_id', 'text_clean', 'stars', 'date']
)
```

## Structure des DataFrames nettoyés

### business_clean.parquet

| Colonne | Type | Description |
|---------|------|-------------|
| business_id | str | ID unique du commerce |
| name | str | Nom du commerce |
| address | str | Adresse |
| city | str | Ville |
| state | str | État |
| postal_code | str | Code postal |
| latitude | float | Latitude |
| longitude | float | Longitude |
| stars | float | Note moyenne (1.0 - 5.0) |
| review_count | int | Nombre d'avis reçus |
| is_open | int | 1 = ouvert, 0 = fermé |
| categories | str | Catégories (séparées par virgules) |

### reviews_clean.parquet

| Colonne | Type | Description |
|---------|------|-------------|
| review_id | str | ID unique de l'avis |
| user_id | str | ID de l'utilisateur |
| business_id | str | ID du commerce |
| stars | int | Note donnée (1-5) |
| text | str | Texte original de l'avis |
| text_clean | str | Texte nettoyé (minuscules, sans URL, etc.) |
| date | datetime | Date de l'avis |
| useful | int | Nombre de votes "utile" |
| funny | int | Nombre de votes "drôle" |
| cool | int | Nombre de votes "cool" |

### users_clean.parquet

| Colonne | Type | Description |
|---------|------|-------------|
| user_id | str | ID unique de l'utilisateur |
| name | str | Nom d'utilisateur |
| review_count | int | Nombre d'avis écrits |
| yelping_since | str | Date d'inscription |
| average_stars | float | Note moyenne donnée |
| useful | int | Total votes "utile" reçus |
| funny | int | Total votes "drôle" reçus |
| cool | int | Total votes "cool" reçus |
| fans | int | Nombre de fans |
| elite | str | Années où l'utilisateur était "elite" |

## Gestion de la mémoire

### Sampler pour tests rapides

```python
# Sampler 10% des données pour prototypage rapide
df_reviews_sample = df_reviews.sample(frac=0.1, random_state=42)
print(f"Sample size: {len(df_reviews_sample):,} reviews")
```

### Charger par chunks (très gros fichiers)

```python
# Charger par morceaux de 100k lignes
chunk_size = 100_000
chunks = []

for chunk in pd.read_parquet(
    'data/cleaned/reviews_clean.parquet',
    chunksize=chunk_size
):
    # Traiter le chunk
    processed_chunk = process(chunk)
    chunks.append(processed_chunk)

df_final = pd.concat(chunks, ignore_index=True)
```

## Checklist du pipeline

**Phase 1 - Chargement:**
- [ ] Business JSON chargé
- [ ] Reviews JSONL chargé
- [ ] Users JSONL chargé
- [ ] Exploration initiale faite (info, describe, head)

**Phase 2 - Nettoyage:**
- [ ] Doublons supprimés
- [ ] Valeurs manquantes gérées
- [ ] Textes nettoyés (reviews)
- [ ] Types de données convertis
- [ ] Validation passée

**Phase 3 - Export:**
- [ ] Dossier `data/cleaned/` créé
- [ ] Fichiers Parquet créés
- [ ] Tailles vérifiées

**Phase 4 - Utilisation:**
- [ ] Chargement Parquet rapide confirmé
- [ ] Colonnes correctement typées
- [ ] Prêt pour analyses

## Problèmes courants

### "FileNotFoundError: data/raw/..."

**Cause:** Fichiers JSON manquants

**Solution:** Téléchargez les données depuis le sujet SAE et placez-les dans `data/raw/`

### "MemoryError" lors du chargement

**Cause:** Fichiers trop gros pour la RAM

**Solution:**
- Utiliser `chunksize` pour charger par morceaux
- Sampler un subset des données
- Charger seulement certaines colonnes

### "UnicodeDecodeError"

**Cause:** Problème d'encodage

**Solution:** Ajouter `encoding='utf-8'` partout

### Parquet très lent à charger

**Cause:** Fichier corrompu ou mal formé

**Solution:** Recréer le fichier Parquet depuis le JSON

## Optimisations avancées

### Compression Parquet

```python
# Utiliser compression pour réduire la taille
df.to_parquet(
    'data/cleaned/reviews_clean.parquet',
    compression='gzip',
    index=False
)
```

### Catégoriser les colonnes répétitives

```python
# Économise de la mémoire pour colonnes avec peu de valeurs uniques
df_reviews['stars'] = df_reviews['stars'].astype('category')
```

## Ressources

- [Pandas Parquet](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html)
- [TQDM Progress Bars](https://tqdm.github.io/)
- Documentation interne: `AI_INSTRUCTIONS.md`

## Prochaines étapes

Après avoir nettoyé les données:
1. Créer des dashboards d'exploration (Epic 1 - Phase 4)
2. Preprocessing NLP (Epic 2)
3. Feature engineering (Epic 3)
