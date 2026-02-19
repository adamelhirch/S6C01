# Utilisation de la librairie partagée dans les notebooks

Le package `src` contient des fonctions réutilisables pour :
- **Chargement de données** (`data_utils.py`)
- **Prétraitement de texte** (`text_preprocessing.py`)
- **Extraction de features** (`features.py`)
- **Visualisation** (`visualization.py`)

## Démarrage rapide

### Importer les fonctions

```python
# Importer des fonctions spécifiques
from src import load_parquet, preprocess_text, compute_tfidf
from src import setup_plot_style, plot_distribution

# Ou importer des modules entiers
from src import data_utils, text_preprocessing, visualization
```

### Exemple 1 : Charger et prétraiter les données

```python
from src import load_parquet, preprocess_text
from tqdm import tqdm

# Charger les reviews
df = load_parquet('reviews_clean.parquet')

# Prétraiter le texte avec barre de progression
tqdm.pandas(desc="Preprocessing")
df['text_clean'] = df['text'].progress_apply(preprocess_text)
```

### Exemple 2 : Analyse TF-IDF

```python
from src import load_parquet, preprocess_text, compute_tfidf

# Charger et prétraiter
df = load_parquet('reviews_clean.parquet', columns=['text'])
df['text_clean'] = df['text'].apply(preprocess_text)

# Calculer TF-IDF
X, vectorizer = compute_tfidf(df['text_clean'].tolist(), max_features=1000)
print(f"Matrice TF-IDF : {X.shape}")
```

### Exemple 3 : Visualisations

```python
from src import load_parquet, setup_plot_style, plot_distribution, plot_top_n

# Configurer un style cohérent
setup_plot_style()

# Charger les données
df = load_parquet('business_clean.parquet')

# Distribution des étoiles
plot_distribution(df['stars'], 'Distribution des étoiles', 'Étoiles', bins=5, save_as='star_dist.png')

# Top villes
top_cities = df['city'].value_counts()
plot_top_n(top_cities, n=10, title='Top 10 Villes', save_as='top_cities.png')
```

### Exemple 4 : Fusion des datasets

```python
from src import load_and_merge, sample_data

# Charger et fusionner tous les datasets
df_full = load_and_merge(
    business_file='business_clean.parquet',
    reviews_file='reviews_clean.parquet',
    users_file='users_clean.parquet'
)

# Échantillonner pour tests rapides
df_sample = sample_data(df_full, n=10000, random_state=42)
```

## Fonctions disponibles

### Data Utils (`data_utils.py`)
- `load_parquet(filename, base_path, columns)` - Charger un Parquet avec gestion d'erreurs
- `load_and_merge(business_file, reviews_file, users_file)` - Fusionner les datasets
- `sample_data(df, n, random_state)` - Échantillonner avec seed reproductible

### Prétraitement de texte (`text_preprocessing.py`)
- `preprocess_text(text)` - Pipeline de prétraitement complet
- `remove_urls_emails(text)` - Supprimer URLs et emails
- `tokenize_and_lemmatize(text, remove_stops)` - Tokeniser et lemmatiser
- `remove_stopwords(tokens)` - Filtrer les stopwords

### Features (`features.py`)
- `compute_tfidf(corpus, max_features)` - Vectorisation TF-IDF

### Visualisation (`visualization.py`)
- `setup_plot_style(style, palette)` - Configurer le style des graphiques
- `save_figure(filename, output_dir, dpi)` - Sauvegarder avec paramètres cohérents
- `plot_distribution(data, title, xlabel, ...)` - Histogrammes
- `plot_top_n(data, n, title, ...)` - Graphiques en barres top N

## Conseils

1. **Toujours importer depuis `src`** en haut des notebooks
2. **Utiliser `setup_plot_style()`** une fois au début pour des visuels cohérents
3. **Utiliser des barres de progression** avec `tqdm` pour les opérations longues
4. **Sauvegarder les graphiques** avec le paramètre `save_as` pour la reproductibilité
