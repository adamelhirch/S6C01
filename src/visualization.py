"""
Visualization utilities for consistent plotting.

This module provides functions for creating and saving plots with
consistent styling across notebooks.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple
from pathlib import Path


def setup_plot_style(style: str = 'seaborn-v0_8-darkgrid', palette: str = 'husl'):
    """
    Configure matplotlib and seaborn plot style.
    
    Args:
        style: Matplotlib style name (default: 'seaborn-v0_8-darkgrid')
        palette: Seaborn color palette (default: 'husl')
    
    Example:
        >>> setup_plot_style()
        >>> # Now all plots will use this style
    """
    plt.style.use(style)
    sns.set_palette(palette)


def save_figure(
    filename: str,
    output_dir: str = 'outputs/figures',
    dpi: int = 300,
    bbox_inches: str = 'tight'
) -> None:
    """
    Save the current figure with consistent settings.
    
    Args:
        filename: Output filename (e.g., 'distribution_stars.png')
        output_dir: Output directory (default: 'outputs/figures')
        dpi: Resolution in dots per inch (default: 300)
        bbox_inches: Bounding box setting (default: 'tight')
    
    Example:
        >>> plt.plot([1, 2, 3], [1, 4, 9])
        >>> save_figure('my_plot.png')
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    filepath = output_path / filename
    plt.savefig(filepath, dpi=dpi, bbox_inches=bbox_inches)
    print(f"Figure saved to: {filepath}")


def plot_distribution(
    data,
    title: str,
    xlabel: str,
    ylabel: str = 'Frequency',
    bins: int = 50,
    color: str = 'skyblue',
    figsize: Tuple[int, int] = (10, 6),
    save_as: Optional[str] = None
) -> None:
    """
    Create a histogram with consistent styling.
    
    Args:
        data: Data to plot
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label (default: 'Frequency')
        bins: Number of bins (default: 50)
        color: Bar color (default: 'skyblue')
        figsize: Figure size as (width, height) (default: (10, 6))
        save_as: Optional filename to save the plot
    
    Example:
        >>> plot_distribution(df['stars'], 'Star Distribution', 'Stars')
    """
    plt.figure(figsize=figsize)
    plt.hist(data, bins=bins, color=color, edgecolor='black', alpha=0.7)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    if save_as:
        save_figure(save_as)
    
    plt.show()


def plot_top_n(
    data,
    n: int = 10,
    title: str = 'Top Items',
    xlabel: str = 'Count',
    color: str = 'coral',
    figsize: Tuple[int, int] = (10, 6),
    save_as: Optional[str] = None
) -> None:
    """
    Create a horizontal bar plot for top N items.
    
    Args:
        data: Series with value counts or similar
        n: Number of top items to show (default: 10)
        title: Plot title
        xlabel: X-axis label (default: 'Count')
        color: Bar color (default: 'coral')
        figsize: Figure size as (width, height) (default: (10, 6))
        save_as: Optional filename to save the plot
    
    Example:
        >>> top_cities = df['city'].value_counts().head(10)
        >>> plot_top_n(top_cities, title='Top 10 Cities')
    """
    plt.figure(figsize=figsize)
    
    # Get top N items
    top_data = data.head(n)
    
    # Create horizontal bar plot
    top_data.plot(kind='barh', color=color)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel('')
    plt.grid(axis='x', alpha=0.3)
    
    # Reverse y-axis to have highest value at top
    plt.gca().invert_yaxis()
    
    if save_as:
        save_figure(save_as)
    
    plt.show()
