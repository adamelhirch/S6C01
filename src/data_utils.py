"""
Data loading utilities for the Yelp dataset project.

This module provides convenient functions for loading cleaned Parquet files.
"""

import pandas as pd
from typing import Optional, List
from pathlib import Path


def load_parquet(
    filename: str,
    base_path: str = 'data/cleaned',
    columns: Optional[List[str]] = None
) -> pd.DataFrame:
    """
    Load a Parquet file with error handling.

    Args:
        filename: Name of the Parquet file (e.g., 'reviews_clean.parquet')
        base_path: Base directory path (default: 'data/cleaned')
        columns: Optional list of columns to load (loads all if None)

    Returns:
        DataFrame with loaded data

    Raises:
        FileNotFoundError: If the file doesn't exist

    Example:
        >>> df = load_parquet('reviews_clean.parquet')
        >>> print(f"Loaded {len(df):,} reviews")
    """
    filepath = Path(base_path) / filename

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_parquet(filepath, columns=columns)
    print(f"Loaded {len(df):,} rows from {filename}")

    return df
