"""
Visualization utilities for consistent plotting.

This module provides functions for creating and saving plots with
consistent styling across notebooks.
"""

import matplotlib.pyplot as plt
import seaborn as sns
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
