# Plan de Projet S6C01 - Analyse Yelp

**Synchronisé avec Linear — Dernière mise à jour: 23 février 2026**

---

## Epic 1 - Setup & Data Loading ✅

| Issue | Titre | État |
|-------|-------|------|
| SAE-58 | Configuration Python venv | ✅ Done |
| SAE-59 | Installation dépendances | ✅ Done |
| SAE-60 | Structure dossiers + .gitignore | ✅ Done |
| SAE-61 | Configuration GitHub | ✅ Done |
| SAE-62 | Configuration Linear + GitHub | ✅ Done |
| SAE-63 | Configuration Jupyter | ✅ Done |
| SAE-64 | Chargement Business JSON | ✅ Done |
| SAE-65 | Chargement Reviews JSON | ✅ Done |
| SAE-66 | Chargement Users JSON | ✅ Done |
| SAE-96 | Nettoyage Business | ✅ Done |
| SAE-97 | Nettoyage Reviews | ✅ Done |
| SAE-98 | Nettoyage Users | ✅ Done |
| SAE-102 | Librairie partagée src/ | ✅ Done |

---

## Epic 2 - Preprocessing & Text Cleaning ✅

| Issue | Titre | État |
|-------|-------|------|
| SAE-70 | Nettoyage texte basique | ✅ Done |
| SAE-71 | Tokenization NLTK | ✅ Done |
| SAE-72 | Suppression stopwords | ✅ Done |
| SAE-73 | Lemmatization | ✅ Done |
| SAE-74 | Pipeline preprocessing complet | ✅ Done |

---

## Epic 3 - Text Representation ✅

| Issue | Titre | Notebook | Grille | État |
|-------|-------|----------|--------|------|
| SAE-76 | TF-IDF optimisé (n-grams) | `3-text-representation/02-tfidf-optimized.ipynb` | Repr N-grammes (1pt) + TF-IDF (1pt) | ✅ Done |
| SAE-77 | Word2Vec training | `3-text-representation/03-word2vec-training.ipynb` | — | ✅ Done |
| SAE-78 | Document embeddings | `3-text-representation/04-document-embeddings.ipynb` | — | ✅ Done |
| SAE-79 | Visualisation t-SNE | `3-text-representation/05-tsne-visualization.ipynb` | — | ✅ Done |
| SAE-80 | Analyse fréquences de mots | `3-text-representation/06-word-frequency-analysis.ipynb` | — | ✅ Done |
| SAE-112 | Extraction embeddings LLM (DistilBERT) | `3-text-representation/05-llm-embeddings.ipynb` | **LLM (1pt)** | ✅ Done |

---

## Epic 4 - ML Classique ✅

**Objectif:** 4 algorithmes (LogReg, SVM, RF, NB) × 3 représentations + sélection variables

| Issue | Titre | Notebook | Grille | État |
|-------|-------|----------|--------|------|
| SAE-114 | Classification ML sur TF-IDF | `4-ML-classique/01-ml-tfidf.ipynb` | ML-tf-idf (1pt) + ML plusieurs (4pts) | ✅ Done |
| SAE-116 | Classification ML sur N-grammes | `4-ML-classique/02-ml-ngram.ipynb` | ML et ngram (1pt) | ✅ Done |
| SAE-117 | Classification ML sur LLM embeddings | `4-ML-classique/03-ml-llm.ipynb` | ML-LLM (1pt) | ✅ Done |
| SAE-118 | Sélection de variables (SHAP) | `4-ML-classique/04-selection-variables.ipynb` | Sélection variables (1pt) | ✅ Done |

---

## Epic 5 - Deep Learning & IA Générative ✅

| Issue | Titre | Notebook | Grille | État |
|-------|-------|----------|--------|------|
| SAE-113 | Deep Learning sur TF-IDF (MLP) | `5-deep-learning/01-deep-tfidf.ipynb` | Deep-tf-idf (1pt) + Arch Deep plusieurs (4pts) | ✅ Done |
| SAE-115 | Deep Learning sur N-grammes (CNN 1D) | `5-deep-learning/02-deep-ngram.ipynb` | Deep-Ngram (1pt) | ✅ Done |
| SAE-119 | Fine-tuning DistilBERT | `5-deep-learning/03-deep-llm.ipynb` | Deep-LLM (1pt) | ✅ Done |
| SAE-124 | IA Générative (Zero-shot, Few-shot, ABSA) | `5-deep-learning/04-ia-generative.ipynb` | Requis sujet B3 | ✅ Done |

---

## Epic 6 - Inférence & Finalisation ✅

| Issue | Titre | Notebook | Grille | État |
|-------|-------|----------|--------|------|
| SAE-120 | Pipeline d'inférence optimal | `6-inference/01-modele-optimal.ipynb` | Modèle optimal (2pts) | ✅ Done |
| SAE-121 | Inférence sur données de test | `6-inference/02-inference-test.ipynb` | Inference test (3pts) | ✅ Done |

---

## Epic 7 - Refactoring & Optimisation

**Objectif:** Refactoriser, simplifier, optimiser. Supprimer le code dupliqué, maximiser la réutilisation via `src/`, améliorer les performances des modèles, et préparer l'évaluation du prof.

### Phase 1 — Modules src/ partagés (pré-requis)

| Issue | Titre | État |
|-------|-------|------|
| SAE-125 | Créer `src/constants.py` — constantes partagées | ⬜ Todo |
| SAE-126 | Créer `src/evaluation.py` — évaluation partagée | ⬜ Todo |
| SAE-127 | Créer `src/ml_utils.py` — utilitaires ML | ⬜ Todo |
| SAE-128 | Créer `src/dl_utils.py` — utilitaires Deep Learning | ⬜ Todo |

### Phase 2 & 3 — Refactoring notebooks

| Issue | Titre | Bloqué par | État |
|-------|-------|------------|------|
| SAE-129 | Refactoring notebooks ML classique | SAE-125/126/127 | ⬜ Todo |
| SAE-130 | Refactoring notebooks Deep Learning | SAE-125/126/128 | ⬜ Todo |

### Phase 4 — Optimisation

| Issue | Titre | Bloqué par | État |
|-------|-------|------------|------|
| SAE-131 | Optimisation modèles — accuracy max sans overfitting | SAE-129/130 | ⬜ Todo |

### Phase 5 & 6 — Évaluation & Nettoyage

| Issue | Titre | Bloqué par | État |
|-------|-------|------------|------|
| SAE-132 | Setup évaluation prof — inférence dataset externe | SAE-131 | ⬜ Todo |
| SAE-133 | Nettoyage final — code propre et exécutable | SAE-129/130/131/132 | ⬜ Todo |

### Ordre d'exécution

```
Phase 1 : SAE-125 + SAE-126 + SAE-127 + SAE-128 (parallélisable)
    ↓
Phase 2 : SAE-129 (ML)  }
Phase 3 : SAE-130 (DL)  } parallélisable
    ↓
Phase 4 : SAE-131 (Optimisation)
    ↓
Phase 5 : SAE-132 (Éval prof)
    ↓
Phase 6 : SAE-133 (Nettoyage final)
```

---

## Grille de notation → Score visé: 24/24

| Critère | Pts | Issue(s) | État |
|---------|-----|----------|------|
| Préparation données | 1 | Epic 1 | ✅ |
| Fonctions inutiles (éviter) | 0 | SAE-133 | ⬜ |
| Sélection variables | 1 | SAE-118 | ✅ |
| Copie/coller naïf (éviter) | 0 | SAE-129/130 | ⬜ |
| Repr N-grammes | 1 | SAE-76 | ✅ |
| Repr TF-IDF | 1 | SAE-76 | ✅ |
| LLM | 1 | SAE-112 | ✅ |
| ML classiques (plusieurs) | **4** | SAE-114/116/117 | ✅ |
| ML + ngram | 1 | SAE-116 | ✅ |
| ML + tf-idf | 1 | SAE-114 | ✅ |
| ML + LLM | 1 | SAE-117 | ✅ |
| Arch Deep (plusieurs) | **4** | SAE-113/115/119 | ✅ |
| Deep-Ngram | 1 | SAE-115 | ✅ |
| Deep-tf-idf | 1 | SAE-113 | ✅ |
| Deep-LLM | 1 | SAE-119 | ✅ |
| Modèle optimal | 2 | SAE-120 | ✅ |
| Inference test | **3** | SAE-121/132 | ✅ |
| **TOTAL** | **24** | | **20/24 critères validés** |

> **Note:** SAE-124 (IA Générative) est requis par le sujet PDF (section B3) mais n'a pas de points directs dans la grille.

> **Attention pénalités:** Les critères "fonctions inutiles" (-1pt) et "copie/coller naïf" (-2pts) seront traités par le refactoring (Epic 7).
