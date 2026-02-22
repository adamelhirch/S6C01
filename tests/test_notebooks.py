"""
Test d'exécution de tous les notebooks du projet.
Lance chaque notebook avec papermill et vérifie qu'il s'exécute sans erreur.

Usage :
    pytest tests/test_notebooks.py -v
    pytest tests/test_notebooks.py -v -k "1-data-loading"    # un seul epic
    pytest tests/test_notebooks.py -v -k "load-business"     # un seul notebook
"""

import os
import glob
import pytest
import papermill as pm

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS_DIR = os.path.join(ROOT_DIR, "notebooks")
OUTPUT_DIR = os.path.join(ROOT_DIR, "tests", "output")


def get_all_notebooks():
    """Récupère tous les .ipynb du projet, triés par epic puis nom."""
    notebooks = glob.glob(os.path.join(NOTEBOOKS_DIR, "**", "*.ipynb"), recursive=True)
    # Exclure les notebooks à la racine de notebooks/ (orphelins)
    notebooks = [nb for nb in notebooks if nb.count(os.sep) > notebooks[0].split("notebooks")[0].count(os.sep) + 1]
    notebooks.sort()
    return notebooks


def notebook_id(path):
    """Génère un ID lisible pour pytest : '1-data-loading/load-business'."""
    rel = os.path.relpath(path, NOTEBOOKS_DIR)
    return rel.replace(".ipynb", "")


ALL_NOTEBOOKS = get_all_notebooks()


@pytest.fixture(scope="session", autouse=True)
def create_output_dir():
    """Crée le dossier de sortie pour les notebooks exécutés."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)


@pytest.mark.parametrize("notebook_path", ALL_NOTEBOOKS, ids=[notebook_id(nb) for nb in ALL_NOTEBOOKS])
def test_notebook_execution(notebook_path):
    """Exécute un notebook et vérifie qu'il ne produit aucune erreur."""
    rel_path = os.path.relpath(notebook_path, NOTEBOOKS_DIR)
    output_path = os.path.join(OUTPUT_DIR, rel_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    pm.execute_notebook(
        notebook_path,
        output_path,
        cwd=os.path.dirname(notebook_path),
        kernel_name="python3",
    )
