# Plan de Projet S6C01 - Analyse Yelp

**Synchronisé avec Linear — Dernière mise à jour: 19 février 2026**

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

## Epic 3 - Text Representation (+ 2 ajouts)

| Issue | Titre | Notebook | Grille | État |
|-------|-------|----------|--------|------|
| **SAE-75** | **TF-IDF basique** | `3-text-representation/01-tfidf-basique.ipynb` | — | ⬜ Todo |
| SAE-76 | TF-IDF optimisé (n-grams) | `3-text-representation/` | Repr N-grammes (1pt) + TF-IDF (1pt) | ✅ Done |
| SAE-77 | Word2Vec training | `3-text-representation/` | — | ✅ Done |
| SAE-78 | Document embeddings | `3-text-representation/` | — | ✅ Done |
| SAE-79 | Visualisation t-SNE | `3-text-representation/` | — | ✅ Done |
| SAE-80 | Analyse fréquences de mots | `3-text-representation/` | — | ✅ Done |
| **SAE-112** | **Extraction embeddings LLM (DistilBERT)** | `3-text-representation/05-llm-embeddings.ipynb` | **LLM (1pt)** | ⬜ Todo |

---

## Epic 4 - ML Classique

**Objectif:** 4 algorithmes (LogReg, SVM, RF, NB) × 3 représentations + sélection variables

**Tâches de prédiction:** Polarité (3 classes) et optionnellement Score (1-5)

| Issue | Titre | Notebook | Grille | État |
|-------|-------|----------|--------|------|
| **SAE-114** | Classification ML sur TF-IDF | `4-ml-classique/01-ml-tfidf.ipynb` | ML-tf-idf (1pt) + ML plusieurs (4pts) | ⬜ Todo |
| **SAE-116** | Classification ML sur N-grammes | `4-ml-classique/02-ml-ngram.ipynb` | ML et ngram (1pt) | ⬜ Todo |
| **SAE-117** | Classification ML sur LLM embeddings | `4-ml-classique/03-ml-llm.ipynb` | ML-LLM (1pt) | ⬜ Todo |
| **SAE-118** | Sélection de variables (SHAP) | `4-ml-classique/04-selection-variables.ipynb` | Sélection variables (1pt) | ⬜ Todo |

**Dépendances:** SAE-117 bloqué par SAE-112. SAE-118 bloqué par SAE-114.

---

## Epic 5 - Deep Learning & IA Générative

**Objectif:** 4 approches (MLP, CNN 1D, DistilBERT fine-tuning, IA Générative) + zero-shot/few-shot + ABSA

**Tâches de prédiction:** Polarité (3 classes) et optionnellement Score (1-5)

| Issue | Titre | Notebook | Grille | État |
|-------|-------|----------|--------|------|
| **SAE-113** | Deep Learning sur TF-IDF (MLP) | `5-deep-learning/01-deep-tfidf.ipynb` | Deep-tf-idf (1pt) + Arch Deep plusieurs (4pts) | ⬜ Todo |
| **SAE-115** | Deep Learning sur N-grammes (CNN 1D) | `5-deep-learning/02-deep-ngram.ipynb` | Deep-Ngram (1pt) | ⬜ Todo |
| **SAE-119** | Fine-tuning DistilBERT | `5-deep-learning/03-deep-llm.ipynb` | Deep-LLM (1pt) | ⬜ Todo |
| **SAE-124** | **IA Générative (Zero-shot, Few-shot, ABSA)** | `5-deep-learning/04-ia-generative.ipynb` | **Requis sujet B3** | ⬜ Todo |

---

## Epic 6 - Inférence & Finalisation

| Issue | Titre | Notebook | Grille | État |
|-------|-------|----------|--------|------|
| **SAE-120** | Pipeline d'inférence optimal | `6-inference/01-modele-optimal.ipynb` | Modèle optimal (2pts) | ⬜ Todo |
| **SAE-121** | Inférence sur données de test | `6-inference/02-inference-test.ipynb` | Inference test (3pts) | ⬜ Todo |
| **SAE-122** | Nettoyage code & fichiers inutiles | — | Éviter pénalités (-3pts) | ⬜ Todo |
| **SAE-123** | Tests pytest | `tests/` | — | ⬜ Todo |

**Dépendances:** SAE-120 bloqué par tous les modèles ML + Deep. SAE-121 bloqué par SAE-120.

---

## Grille de notation → Score visé: 24/24

| Critère | Pts | Issue(s) |
|---------|-----|----------|
| Préparation données | 1 | ✅ Epic 1 |
| Fonctions inutiles (éviter) | 0 | SAE-122 |
| Sélection variables | 1 | SAE-118 |
| Copie/coller naïf (éviter) | 0 | SAE-122 |
| Repr N-grammes | 1 | ✅ SAE-76 |
| Repr TF-IDF | 1 | ✅ SAE-76 |
| LLM | 1 | SAE-112 |
| ML classiques (plusieurs) | **4** | SAE-114/116/117 |
| ML + ngram | 1 | SAE-116 |
| ML + tf-idf | 1 | SAE-114 |
| ML + LLM | 1 | SAE-117 |
| Arch Deep (plusieurs) | **4** | SAE-113/115/119 |
| Deep-Ngram | 1 | SAE-115 |
| Deep-tf-idf | 1 | SAE-113 |
| Deep-LLM | 1 | SAE-119 |
| Modèle optimal | 2 | SAE-120 |
| Inference test | **3** | SAE-121 |
| **TOTAL** | **24** | |

> **Note:** SAE-124 (IA Générative) est requis par le sujet PDF (section B3) mais n'a pas de points directs dans la grille.

---

## Ordre d'exécution

1. SAE-112 — LLM embeddings (pré-requis)
2. SAE-114 + SAE-116 — ML TF-IDF + ML N-grammes (parallélisable)
3. SAE-117 — ML LLM (après SAE-112)
4. SAE-118 — Sélection variables
5. SAE-113 + SAE-115 — Deep TF-IDF + Deep N-grammes (parallélisable)
6. SAE-119 — Fine-tuning DistilBERT
7. SAE-124 — IA Générative (zero-shot, few-shot, ABSA)
8. SAE-120 — Pipeline optimal
9. SAE-121 — Inference test
10. SAE-122 + SAE-123 — Nettoyage + tests
