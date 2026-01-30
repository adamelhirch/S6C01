"""
Fonctions utilitaires pour le chargement des données Yelp
"""
import pandas as pd
import json
from pathlib import Path


def load_yelp_json(filepath, nrows=None):
    """
    Charge un fichier JSON Yelp (format NDJSON - une ligne par objet)

    Args:
        filepath: Chemin vers le fichier JSON
        nrows: Nombre de lignes à charger (None = tout charger)

    Returns:
        DataFrame pandas
    """
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if nrows and i >= nrows:
                break
            data.append(json.loads(line))

    return pd.DataFrame(data)


def save_to_parquet(df, filepath):
    """
    Sauvegarde un DataFrame en format Parquet

    Args:
        df: DataFrame pandas
        filepath: Chemin de destination
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(filepath, index=False)
    print(f"✅ Sauvegardé: {filepath} ({len(df)} lignes)")


def load_parquet(filepath):
    """
    Charge un fichier Parquet

    Args:
        filepath: Chemin vers le fichier Parquet

    Returns:
        DataFrame pandas
    """
    df = pd.read_parquet(filepath)
    print(f"✅ Chargé: {filepath} ({len(df)} lignes)")
    return df
