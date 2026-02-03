# 📚 Using the Shared Library in Notebooks

The `src` package now contains reusable functions for:
- **Data loading** (`data_utils.py`)
- **Text preprocessing** (`text_preprocessing.py`)
- **Feature extraction** (`features.py`)
- **Visualization** (`visualization.py`)

## Quick Start

### Import Functions

```python
# Import specific functions
from src import load_parquet, preprocess_text, compute_tfidf
from src import setup_plot_style, plot_distribution

# Or import entire modules
from src import data_utils, text_preprocessing, visualization
```

### Example 1: Load and Preprocess Data

```python
from src import load_parquet, preprocess_text
from tqdm import tqdm

# Load reviews
df = load_parquet('reviews_clean.parquet')

# Preprocess text with progress bar
tqdm.pandas(desc="Preprocessing")
df['text_clean'] = df['text'].progress_apply(preprocess_text)
```

### Example 2: TF-IDF Analysis

```python
from src import load_parquet, preprocess_text, compute_tfidf

# Load and preprocess
df = load_parquet('reviews_clean.parquet', columns=['text'])
df['text_clean'] = df['text'].apply(preprocess_text)

# Compute TF-IDF
X, vectorizer = compute_tfidf(df['text_clean'].tolist(), max_features=1000)
print(f"TF-IDF matrix shape: {X.shape}")
```

### Example 3: Visualizations

```python
from src import load_parquet, setup_plot_style, plot_distribution, plot_top_n

# Setup consistent style
setup_plot_style()

# Load data
df = load_parquet('business_clean.parquet')

# Plot star distribution
plot_distribution(df['stars'], 'Star Distribution', 'Stars', bins=5, save_as='star_dist.png')

# Plot top cities
top_cities = df['city'].value_counts()
plot_top_n(top_cities, n=10, title='Top 10 Cities', save_as='top_cities.png')
```

### Example 4: Merge Datasets

```python
from src import load_and_merge, sample_data

# Load and merge all datasets
df_full = load_and_merge(
    business_file='business_clean.parquet',
    reviews_file='reviews_clean.parquet',
    users_file='users_clean.parquet'
)

# Sample for quick testing
df_sample = sample_data(df_full, n=10000, random_state=42)
```

## Available Functions

### Data Utils (`data_utils.py`)
- `load_parquet(filename, base_path, columns)` - Load Parquet with error handling
- `load_and_merge(business_file, reviews_file, users_file)` - Merge datasets
- `sample_data(df, n, random_state)` - Sample with reproducible seed

### Text Preprocessing (`text_preprocessing.py`)
- `preprocess_text(text)` - Complete preprocessing pipeline
- `remove_urls_emails(text)` - Remove URLs and emails
- `tokenize_and_lemmatize(text, remove_stops)` - Tokenize and lemmatize
- `remove_stopwords(tokens)` - Filter stopwords from tokens

### Features (`features.py`)
- `compute_tfidf(corpus, max_features)` - TF-IDF vectorization

### Visualization (`visualization.py`)
- `setup_plot_style(style, palette)` - Configure plot styling
- `save_figure(filename, output_dir, dpi)` - Save with consistent settings
- `plot_distribution(data, title, xlabel, ...)` - Histogram plots
- `plot_top_n(data, n, title, ...)` - Top N bar plots

## Tips

1. **Always import from `src`** at the top of notebooks
2. **Use `setup_plot_style()`** once at the beginning for consistent visuals
3. **Use progress bars** with `tqdm` for long operations
4. **Save plots** with `save_as` parameter for reproducibility
