"""
Data loading utilities for the Yelp dataset project.

This module provides convenient functions for loading and manipulating
cleaned Parquet files.
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


def load_and_merge(
    business_file: str = 'business_clean.parquet',
    reviews_file: str = 'reviews_clean.parquet',
    users_file: Optional[str] = None,
    base_path: str = 'data/cleaned'
) -> pd.DataFrame:
    """
    Load and merge business, reviews, and optionally users data.
    
    Args:
        business_file: Business Parquet filename
        reviews_file: Reviews Parquet filename
        users_file: Optional users Parquet filename
        base_path: Base directory path
    
    Returns:
        Merged DataFrame
    
    Example:
        >>> df = load_and_merge()
        >>> print(df.columns.tolist())
    """
    # Load business and reviews
    df_business = load_parquet(business_file, base_path)
    df_reviews = load_parquet(reviews_file, base_path)
    
    # Merge on business_id
    df_merged = df_reviews.merge(df_business, on='business_id', how='left', suffixes=('_review', '_business'))
    print(f"Merged business and reviews: {len(df_merged):,} rows")
    
    # Optionally merge users
    if users_file:
        df_users = load_parquet(users_file, base_path)
        df_merged = df_merged.merge(df_users, on='user_id', how='left', suffixes=('', '_user'))
        print(f"Merged with users: {len(df_merged):,} rows")
    
    return df_merged


def sample_data(
    df: pd.DataFrame,
    n: int = 10000,
    random_state: int = 42
) -> pd.DataFrame:
    """
    Sample data with reproducible random seed.
    
    Args:
        df: Input DataFrame
        n: Number of rows to sample
        random_state: Random seed for reproducibility (default: 42)
    
    Returns:
        Sampled DataFrame
    
    Example:
        >>> df_sample = sample_data(df, n=5000)
        >>> print(f"Sampled {len(df_sample):,} rows")
    """
    if n >= len(df):
        print(f"Warning: Sample size {n:,} >= dataset size {len(df):,}, returning full dataset")
        return df
    
    df_sample = df.sample(n=n, random_state=random_state)
    print(f"Sampled {len(df_sample):,} rows from {len(df):,} (random_state={random_state})")
    
    return df_sample
