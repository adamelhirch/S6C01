"""
S6C01 Yelp Dataset Analysis - Shared Utilities Library

This package provides reusable functions for working with the Yelp dataset.

Example:
    >>> from src.data_utils import load_parquet
    >>> from src.text_preprocessing import clean_text
    >>> from src.ml_utils import load_and_prepare, split_data
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

# Constants
from .constants import (
    RANDOM_STATE,
    SAMPLE_SIZE,
    POLARITY_NAMES,
    SCORE_NAMES,
    stars_to_polarity,
)

# Evaluation
from .evaluation import (
    compute_metrics,
    evaluate_classifier,
    plot_confusion,
    plot_training_curves,
    print_report,
)

# ML utilities
from .ml_utils import (
    load_and_prepare,
    split_data,
    get_param_grids,
    tune_and_evaluate,
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
    # Constants
    'RANDOM_STATE',
    'SAMPLE_SIZE',
    'POLARITY_NAMES',
    'SCORE_NAMES',
    'stars_to_polarity',
    # Evaluation
    'compute_metrics',
    'evaluate_classifier',
    'plot_confusion',
    'plot_training_curves',
    'print_report',
    # ML utilities
    'load_and_prepare',
    'split_data',
    'get_param_grids',
    'tune_and_evaluate',
]
