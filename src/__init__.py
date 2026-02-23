"""
S6C01 Yelp Dataset Analysis - Shared Utilities Library

This package provides reusable functions for working with the Yelp dataset.

Example:
    >>> from src.data_utils import load_parquet
    >>> from src.text_preprocessing import clean_text
    >>> df = load_parquet('reviews_clean.parquet')
"""

# Data loading utilities
from .data_utils import load_parquet

# Text preprocessing
from .text_preprocessing import (
    clean_text,
    remove_urls_emails,
    remove_stopwords,
    preprocess_pipeline,
    tokenize_text,
    lemmatize_tokens,
)

# Visualization utilities
from .visualization import (
    setup_plot_style,
    save_figure,
)

__all__ = [
    # Data utilities
    'load_parquet',
    # Text preprocessing
    'clean_text',
    'remove_urls_emails',
    'remove_stopwords',
    'preprocess_pipeline',
    'tokenize_text',
    'lemmatize_tokens',
    # Visualization
    'setup_plot_style',
    'save_figure',
]
