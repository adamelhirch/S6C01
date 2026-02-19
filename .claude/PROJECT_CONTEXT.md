# PROJECT CONTEXT - S6C01 Yelp Analysis

## Vue d'ensemble

- **Type**: Data Science / ML / NLP — Classification de sentiment sur Yelp
- **Niveau**: BUT Informatique S6 (2025-2026)
- **Stack**: Python 3.12+, Pandas, Scikit-learn, PyTorch, HuggingFace
- **Méthodologie**: Agile (Linear) + Git/GitHub
- **Prédictions**: Polarité (3 classes: positif/neutre/négatif) + Score (1-5 étoiles)

## Équipe

- Adam EL HIRCH (@adamelhirch), Natalia ROS (@rsnataliaa), Ewen MONTOUT (@ewen-montout), Manolo BRACH (@reyyko), Lotfi MELOUANE (@lotfimln)

## Structure

```
S6C01/
├── data/raw/ (JSON, non versionnés) → data/cleaned/ (Parquet + embeddings)
├── notebooks/
│   ├── 1-data-loading/          ✅ Done
│   ├── 2-preprocessing/         ✅ Done
│   ├── 3-text-representation/   ✅ Done (+SAE-112 LLM à faire)
│   ├── 4-ml-classique/          ⬜ SAE-114, 116, 117, 118
│   ├── 5-deep-learning/         ⬜ SAE-113, 115, 119, 124
│   └── 6-inference/             ⬜ SAE-120, 121
├── src/                         Librairie partagée (data_utils, text_preprocessing, features, visualization)
├── tests/                       ⬜ SAE-123 (pytest)
└── outputs/figures/ + models/
```

## Epics et issues actives

### Epic 1-3: ✅ DONE (Setup, Preprocessing, Text Representation)

### Epic 3 ajout:
- **SAE-112**: Extraction embeddings LLM (DistilBERT) → `3-text-representation/05-llm-embeddings.ipynb`

### Epic 4 - ML Classique (4 algos × 3 représentations):
- **SAE-114**: ML sur TF-IDF (LogReg, SVM, RF, NB) → `4-ml-classique/01-ml-tfidf.ipynb`
- **SAE-116**: ML sur N-grammes → `4-ml-classique/02-ml-ngram.ipynb`
- **SAE-117**: ML sur LLM embeddings → `4-ml-classique/03-ml-llm.ipynb` (bloqué par SAE-112)
- **SAE-118**: Sélection variables (SHAP) → `4-ml-classique/04-selection-variables.ipynb`

### Epic 5 - Deep Learning & IA Générative (4 approches):
- **SAE-113**: MLP sur TF-IDF → `5-deep-learning/01-deep-tfidf.ipynb`
- **SAE-115**: CNN 1D sur N-grammes → `5-deep-learning/02-deep-ngram.ipynb`
- **SAE-119**: Fine-tuning DistilBERT → `5-deep-learning/03-deep-llm.ipynb`
- **SAE-124**: IA Générative (zero-shot, few-shot, ABSA) → `5-deep-learning/04-ia-generative.ipynb`

### Epic 6 - Inférence & Finalisation:
- **SAE-120**: Pipeline optimal → `6-inference/01-modele-optimal.ipynb` (bloqué par tous les modèles)
- **SAE-121**: Inference test → `6-inference/02-inference-test.ipynb` (bloqué par SAE-120)
- **SAE-122**: Nettoyage code
- **SAE-123**: Tests pytest

## Workflow Git + Linear

### Branches
Format: `prenom/sae-XX-description`

### Commits
Format: `SAE-XX Description`

### Quand une story est terminée (automatique):
1. Créer PR avec `mcp__github__create_pull_request` (owner: adamelhirch, repo: S6C01, base: main)
2. Ajouter lien PR dans Linear avec `mcp__linear-server__update_issue`
3. Mettre la story en "In Review"

### Format des liens Linear:
- Branche: `{"title": "Branche GitHub: {nom}", "url": "https://github.com/adamelhirch/S6C01/tree/{nom}"}`
- PR: `{"title": "PR #{num}: {titre}", "url": "https://github.com/adamelhirch/S6C01/pull/{num}"}`

**IMPORTANT:** Toujours AJOUTER aux liens existants, JAMAIS les remplacer.

## Points critiques

- Fichiers JSON non versionnés (~6 GB)
- Toujours activer venv: `source venv/bin/activate`
- Jamais de commits directs sur main
- 1 notebook = 1 issue = 1 critère de notation
- Éviter code inutile (pénalité -1pt) et copier-coller naïf (pénalité -2pts)
- Deux tâches de prédiction: polarité (3 classes) + score (1-5)

## Grille de notation (24 pts max)

Voir `docs/PROJECT-PLAN.md` pour le mapping complet issues → critères.
