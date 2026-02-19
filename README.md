# S6C01 - Analyse de Données Yelp

**SAE S6C01 - Analyse de Grandes Données**
**BUT Informatique - Semestre 6 (2025-2026)**

## Équipe

- **Adam EL HIRCH** - [@adamelhirch](https://github.com/adamelhirch)
- **Natalia ROS** - [@rsnataliaa](https://github.com/rsnataliaa)
- **Ewen MONTOUT** - [@ewen-montout](https://github.com/ewen-montout)
- **Manolo BRACH** - [@reyyko](https://github.com/reyyko)
- **Lotfi MELOUANE** - [@lotfimln](https://github.com/lotfimln)

## Description

Analyse du dataset Yelp Academic avec Python, NLP et Machine Learning.
Classification de sentiment sur les avis clients avec ML classique, Deep Learning et IA Générative.

## Structure du Projet

```
S6C01/
├── data/
│   ├── raw/                          # JSON bruts Yelp (non versionnés)
│   └── cleaned/                      # Parquet nettoyés (non versionnés)
├── notebooks/
│   ├── 1-data-loading/               # Chargement JSON → Parquet
│   ├── 2-preprocessing/              # NLP: tokenization, stopwords, lemmatization
│   ├── 3-text-representation/        # TF-IDF, Word2Vec, LLM embeddings
│   ├── 4-ml-classique/               # ML: LogReg, SVM, RF, NB × 3 représentations
│   ├── 5-deep-learning/              # Deep: MLP, CNN 1D, DistilBERT, IA Générative
│   └── 6-inference/                  # Pipeline optimal + test
├── src/                              # Librairie Python partagée
├── tests/                            # Tests pytest
├── outputs/
│   ├── figures/                      # Visualisations
│   └── models/                       # Modèles sauvegardés
├── docs/                             # Documentation
│   └── PROJECT-PLAN.md               # Plan synchronisé avec Linear
└── sujet/                            # PDF du sujet et cours
```

## Epics

| Epic | Objectif | État |
|------|----------|------|
| 1 - Setup & Data Loading | Environnement + chargement/nettoyage JSON | ✅ Done |
| 2 - Preprocessing | NLP: tokenization, stopwords, lemmatization | ✅ Done |
| 3 - Text Representation | TF-IDF, Word2Vec, LLM embeddings | ✅ Done |
| 4 - ML Classique | 4 algos × 3 représentations + sélection variables | Todo |
| 5 - Deep Learning | MLP + CNN 1D + DistilBERT + IA Générative | Todo |
| 6 - Inférence & Finalisation | Pipeline optimal + test + nettoyage | Todo |

## Installation

```bash
git clone https://github.com/adamelhirch/S6C01-Yelp-Analysis.git
cd S6C01-Yelp-Analysis
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

Placer les fichiers JSON Yelp dans `data/raw/`.

## Workflow

1. Prendre une issue sur [Linear](https://linear.app/sae6c01)
2. Créer une branche: `git checkout -b prenom/sae-XX-description`
3. Développer, commiter: `SAE-XX Description`
4. Pousser, créer une PR, review, merge

## Technologies

- Python 3.12+, Pandas, NumPy
- NLTK, Scikit-learn (NLP + ML classique)
- PyTorch, HuggingFace Transformers (Deep Learning)
- Jupyter Notebooks

## Progression

Suivi sur [Linear](https://linear.app/sae6c01) — voir `docs/PROJECT-PLAN.md` pour le détail.
