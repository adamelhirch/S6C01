"""
S6C01 Yelp Dataset Analysis - Shared Utilities Library

This package provides reusable functions for working with the Yelp dataset.
Import commonly used functions directly from the package.

Example:
    >>> from src import load_parquet, preprocess_text, compute_tfidf
    >>> df = load_parquet('reviews_clean.parquet')
    >>> df['text_clean'] = df['text'].apply(preprocess_text)
"""

# Data loading utilities
from .data_utils import (
    load_parquet,
    load_and_merge,
    sample_data
)

# Text preprocessing
from .text_preprocessing import (
    preprocess_text,
    remove_urls_emails,
    tokenize_and_lemmatize,
    remove_stopwords
)

# Feature extraction
from .features import (
    compute_tfidf
)

# Visualization utilities
from .visualization import (
    setup_plot_style,
    save_figure,
    plot_distribution,
    plot_top_n
)

__all__ = [
    # Data utilities
    'load_parquet',
    'load_and_merge',
    'sample_data',
    # Text preprocessing
    'preprocess_text',
    'remove_urls_emails',
    'tokenize_and_lemmatize',
    'remove_stopwords',
    # Features
    'compute_tfidf',
    # Visualization
    'setup_plot_style',
    'save_figure',
    'plot_distribution',
    'plot_top_n',
]
