# Rapport de Traçabilité — S6C01 Analyse Yelp

**Date :** 20 février 2026
**Auteur :** Adam El Hirch

---

## 1. Synthèse : Stories liées au sujet / cours / grille / aucun

### Légende

| Symbole | Signification |
|:-------:|---------------|
| ✅ | Référence explicite trouvée |
| 🔶 | Référence implicite (nécessaire mais pas nommé) |
| ❌ | Aucune référence |

---

### Tableau récapitulatif complet

| Story | Titre | Sujet PDF | Cours | Grille | Verdict |
|-------|-------|:---------:|:-----:|:------:|---------|
| **Epic 1 — Data Loading** |||||
| SAE-64 | Chargement Business JSON | ✅ | ❌ | 🔶 | **Requis sujet** |
| SAE-65 | Chargement Reviews JSON | ✅ | ❌ | 🔶 | **Requis sujet** |
| SAE-66 | Chargement Users JSON | ✅ | ❌ | 🔶 | **Requis sujet** |
| SAE-96 | Nettoyage Business | 🔶 | ❌ | 🔶 | **Requis sujet** (implicite) |
| SAE-97 | Nettoyage Reviews | 🔶 | ❌ | 🔶 | **Requis sujet** (implicite) |
| SAE-98 | Nettoyage Users | 🔶 | ❌ | 🔶 | **Requis sujet** (implicite) |
| SAE-102 | Librairie partagée src/ | ❌ | ❌ | ❌ | **Non requis** — bonne pratique |
| **Epic 2 — Preprocessing** |||||
| SAE-70 | Nettoyage texte basique | 🔶 | ✅ | 🔶 | **Requis cours** |
| SAE-71 | Tokenization NLTK | 🔶 | ✅ | 🔶 | **Requis cours** |
| SAE-72 | Suppression stopwords | 🔶 | ✅ | 🔶 | **Requis cours** |
| SAE-73 | Lemmatization | 🔶 | ✅ | 🔶 | **Requis cours** |
| SAE-74 | Pipeline preprocessing | 🔶 | ✅ | 🔶 | **Requis cours** |
| **Epic 3 — Text Representation** |||||
| SAE-75 | TF-IDF basique | ✅ | ✅ | ❌ | **Requis sujet + cours** |
| SAE-76 | TF-IDF optimisé (n-grams) | ❌ | ✅ | ✅ | **Requis cours + grille** |
| SAE-77 | Word2Vec training | ❌ | ✅ | ❌ | **Couvert cours** — bonus |
| SAE-78 | Document embeddings | ❌ | 🔶 | ❌ | **Non requis** — bonus |
| SAE-79 | Visualisation t-SNE | ❌ | ❌ | ❌ | **Non requis** — bonus |
| SAE-80 | Analyse fréquences de mots | ✅ | ❌ | ❌ | **Requis sujet** |
| SAE-112 | Embeddings LLM (DistilBERT) | ✅ | ✅ | ✅ | **Requis sujet + cours + grille** |
| **Epic 4 — ML Classique** |||||
| SAE-114 | ML sur TF-IDF | ✅ | ✅ | ✅ | **Requis sujet + cours + grille** |
| SAE-116 | ML sur N-grammes | ❌ | 🔶 | ✅ | **Requis grille** |
| SAE-117 | ML sur LLM embeddings | ✅ | 🔶 | ✅ | **Requis sujet + grille** |
| SAE-118 | Sélection de variables (SHAP) | ❌ | ❌ | ✅ | **Requis grille uniquement** |
| **Epic 5 — Deep Learning & IA Générative** |||||
| SAE-113 | Deep Learning TF-IDF (MLP) | ✅ | ✅ | ✅ | **Requis sujet + cours + grille** |
| SAE-115 | Deep Learning N-grammes (CNN) | ✅ | ✅ | ✅ | **Requis sujet + cours + grille** |
| SAE-119 | Fine-tuning DistilBERT | ✅ | ✅ | ✅ | **Requis sujet + cours + grille** |
| SAE-124 | IA Générative (Zero/Few-shot, ABSA) | ✅ | ✅ | ❌ | **Requis sujet + cours** (0pt grille) |
| **Epic 6 — Inférence & Finalisation** |||||
| SAE-120 | Pipeline d'inférence optimal | 🔶 | ❌ | ✅ | **Requis grille** |
| SAE-121 | Inférence sur données de test | 🔶 | ❌ | ✅ | **Requis grille** |
| SAE-122 | Nettoyage code & fichiers inutiles | ❌ | ❌ | ✅ | **Requis grille** (pénalités) |
| SAE-123 | Tests pytest | ❌ | ❌ | ❌ | **Non requis** — bonne pratique |

---

## 2. Détail des références par story

### Epic 1 — Data Loading ✅ Done

#### SAE-64/65/66 — Chargement Business/Reviews/Users
- **Sujet (p.1) :** « Ce jeu de données [...] est composé de plusieurs fichiers, dont notamment : review.json [...] business.json [...] user.json »
- **Cours :** Aucune mention
- **Grille :** Couvert par « Préparation données (1pt) »

#### SAE-96/97/98 — Nettoyage Business/Reviews/Users
- **Sujet (p.2) :** « Avant de se lancer dans la phase de prédiction, il est demandé d'effectuer quelques analyses afin de mieux comprendre la répartition des données »
- **Cours :** Aucune mention
- **Grille :** Couvert par « Préparation données (1pt) »

#### SAE-102 — Librairie partagée src/
- **Sujet :** ❌ Aucune mention
- **Cours :** ❌ Aucune mention
- **Grille :** ❌ Non noté — bonne pratique pour éviter le copier-coller (pénalité -2pts)

---

### Epic 2 — Preprocessing ✅ Done

#### SAE-70 à SAE-74 — Pipeline de prétraitement
- **Sujet :** Aucune mention explicite du prétraitement. Implicite pour toute tâche NLP.
- **Cours Text Representation (p.16) :** « Segmenter les séquences de caractères en mots, en sous mots, … (Tokenizing) — Normaliser — Textuelle: ponctuation, dates, case — Linguistique : Racinisation (stemming)/lemmatisation — Supprimer les mots communs (stop word removal) »
- **Grille :** Couvert par « Préparation données (1pt) »

---

### Epic 3 — Text Representation (5/7 Done)

#### SAE-75 — TF-IDF basique ⬜ Todo
- **Sujet (p.2) :** « Plusieurs représentations du texte : mots simples (sac de mots / bag-of-words), **TF-IDF** »
- **Cours Text Representation (p.19) :** « Pondération tf.idf — tf : Fréquence du terme dans le document — idf : fréquence (inverse) du terme dans la collection »
- **Grille :** Pas de point spécifique (couvert par SAE-76)

#### SAE-76 — TF-IDF optimisé (n-grams) ✅ Done
- **Sujet :** ❌ Pas de mention explicite des n-grammes
- **Cours Text Representation (p.30) :** « basées sur n-grams (exemple bigrams) (prendre les mots 2 à 2 avec overlap) »
- **Grille :** Repr N-grammes (1pt) + Repr TF-IDF (1pt)

#### SAE-77 — Word2Vec training ✅ Done
- **Sujet :** ❌ Aucune mention
- **Cours Text Representation (p.27-34) :** « Approche Word2Vec — apprentissage d'un modèle neuronal simple (peu profond) à partir d'un grand corpus de textes »
- **Grille :** ❌ Non noté

#### SAE-78 — Document embeddings ✅ Done
- **Sujet :** ❌ Aucune mention
- **Cours :** 🔶 Implicite (passage mot → document)
- **Grille :** ❌ Non noté

#### SAE-79 — Visualisation t-SNE ✅ Done
- **Sujet :** ❌ Aucune mention
- **Cours :** ❌ Aucune mention
- **Grille :** ❌ Non noté

#### SAE-80 — Analyse fréquences de mots ✅ Done
- **Sujet (p.2) :** « Comparer les vocabulaires dans les avis négatifs et les avis positifs (sélectionner les 10 tops mots en utilisant par exemple tf.idf) »
- **Cours :** ❌ Aucune mention
- **Grille :** ❌ Non noté directement (fait partie de la section A)

#### SAE-112 — Embeddings LLM (DistilBERT) ⬜ Todo
- **Sujet (p.2) :** « **Embeddings issus de modèles pré-entraînés de type BERT** ou un LLM de type GPT »
- **Cours IA Générative (p.36) :** « Modèles issus de BERT : Roberta, **DistilBERT**, ALBERT, TinyBERT, CammeBERT, CodeBERT... »
- **Cours Text Representation (p.35-37) :** « Embeddings Contextuels — Combiner Word Embeddings et Modèle de langage — GPT, BERT, … »
- **Grille :** LLM (1pt)

---

### Epic 4 — ML Classique (0/4 Done)

#### SAE-114 — Classification ML sur TF-IDF ⬜ Todo
- **Sujet (p.3) :** « des algorithmes "classiques" de Machine Learning (**régression logistique, SVM**, etc.) »
- **Sujet (p.2) :** « Deux tâches de prédiction sont attendues : 1. Prédiction de la polarité [...] 2. Prédiction du score (rating) »
- **Cours Text Representation (p.7-8) :** « Classification de textes — Analyse de sentiments »
- **Grille :** ML + tf-idf (1pt) + ML classiques plusieurs (4pts)

#### SAE-116 — Classification ML sur N-grammes ⬜ Todo
- **Sujet :** ❌ Pas de mention explicite de ML + N-grammes
- **Cours :** 🔶 Implicite (n-grams + classification = combinaison logique)
- **Grille :** ML + ngram (1pt) — **Requis pour les 4pts "ML classiques plusieurs"**

#### SAE-117 — Classification ML sur LLM embeddings ⬜ Todo
- **Sujet (p.2-3) :** « Ces représentations [dont embeddings BERT/LLM] devront être **évaluées et comparées** dans le cadre des tâches de classification »
- **Cours :** 🔶 Implicite (embeddings BERT + ML classique)
- **Grille :** ML + LLM (1pt) — **Requis pour les 4pts "ML classiques plusieurs"**

#### SAE-118 — Sélection de variables (SHAP) ⬜ Todo
- **Sujet :** ❌ Aucune mention de sélection de variables ni de SHAP
- **Cours :** ❌ Aucune mention
- **Grille :** Sélection variables (1pt) — **Requis grille uniquement**

---

### Epic 5 — Deep Learning & IA Générative (0/4 Done)

#### SAE-113 — Deep Learning sur TF-IDF (MLP) ⬜ Todo
- **Sujet (p.3) :** « **SURTOUT des modèles de Deep Learning (MLP** ou CNN) »
- **Cours IA Générative (p.3) :** « Deep ML utile pour le traitement de la langue [...] LSTM, CNN, LLM »
- **Grille :** Deep-tf-idf (1pt) + Arch Deep plusieurs (4pts)

#### SAE-115 — Deep Learning sur N-grammes (CNN 1D) ⬜ Todo
- **Sujet (p.3) :** « SURTOUT des modèles de Deep Learning (MLP ou **CNN**) »
- **Cours IA Générative (p.3) :** « LSTM, **CNN**, LLM »
- **Grille :** Deep-Ngram (1pt) — **Requis pour les 4pts "Arch Deep plusieurs"**

#### SAE-119 — Fine-tuning DistilBERT ⬜ Todo
- **Sujet (p.3) :** « **Au moins un modèle basé sur l'architecture Transformer** (prendre un modèle déjà finetuné ou à fine tuner vous-même) »
- **Cours IA Générative (p.18) :** « Fine tuning du modèle pour une tâche spécifique »
- **Cours IA Générative (p.27) :** « Fine-Tuning Supervisé — Finetuning traditionnel pour des tâches spécifiques en fournissant des exemples »
- **Grille :** Deep-LLM (1pt) — **Requis pour les 4pts "Arch Deep plusieurs"**

#### SAE-124 — IA Générative (Zero-shot, Few-shot, ABSA) ⬜ Todo
- **Sujet (p.3, section B3 entière) :** « **Utilisation d'une IA générative** — Classification en zero-shot et few-shot — Extraction d'aspects (Aspect-Based Sentiment Analysis) »
- **Cours IA Générative (p.52) :** « Apprentissage en contexte (In Context Learning), le modèle peut résoudre des tâches simplement en recevant une consigne (prompt) — "zero-shot" (consigne avec 0 exemple) ou "few-shot learning" (consigne avec quelques exemples) »
- **Cours Text Representation (p.8) :** « Extraction de facettes — Sur quels éléments porte la revue [...] portent le sentiment »
- **Grille :** ❌ Pas de points directs — **Mais requis obligatoirement par le sujet**

---

### Epic 6 — Inférence & Finalisation (0/4 Done)

#### SAE-120 — Pipeline d'inférence optimal ⬜ Todo
- **Sujet :** 🔶 Implicite — choisir le meilleur modèle parmi tous ceux testés
- **Cours :** ❌ Aucune mention
- **Grille :** Modèle optimal (2pts)

#### SAE-121 — Inférence sur données de test ⬜ Todo
- **Sujet :** 🔶 Implicite — évaluer sur données non vues
- **Cours :** ❌ Aucune mention
- **Grille :** Inference test (**3pts** — critère le plus lourd)

#### SAE-122 — Nettoyage code & fichiers inutiles ⬜ Todo
- **Sujet :** ❌ Aucune mention
- **Cours :** ❌ Aucune mention
- **Grille :** Pénalités — Fonctions inutiles (-1pt) + Copier-coller naïf (-2pts)

#### SAE-123 — Tests pytest ⬜ Todo
- **Sujet :** ❌ Aucune mention
- **Cours :** ❌ Aucune mention
- **Grille :** ❌ Non noté

---

## 3. Résumé par catégorie

### ✅ Requis par le sujet ET le cours ET la grille (6 stories — 14pts)

| Story | Titre | Pts grille |
|-------|-------|:----------:|
| SAE-112 | Embeddings LLM (DistilBERT) | 1pt |
| SAE-114 | ML sur TF-IDF | 1pt + 4pts partagés |
| SAE-113 | Deep Learning TF-IDF (MLP) | 1pt + 4pts partagés |
| SAE-115 | Deep Learning N-grammes (CNN) | 1pt |
| SAE-119 | Fine-tuning DistilBERT | 1pt |
| SAE-124 | IA Générative | 0pt (mais **obligatoire**) |

### ✅ Requis par le sujet uniquement (2 stories — 0pt direct)

| Story | Titre | Pts grille |
|-------|-------|:----------:|
| SAE-75 | TF-IDF basique | — (couvert par SAE-76) |
| SAE-117 | ML sur LLM embeddings | 1pt |

### ✅ Requis par le cours + grille (1 story)

| Story | Titre | Pts grille |
|-------|-------|:----------:|
| SAE-76 | TF-IDF optimisé (n-grams) | 2pts (✅ Done) |

### ✅ Requis par la grille uniquement (5 stories — 10pts)

| Story | Titre | Pts grille |
|-------|-------|:----------:|
| SAE-116 | ML sur N-grammes | 1pt |
| SAE-118 | Sélection de variables (SHAP) | 1pt |
| SAE-120 | Pipeline optimal | 2pts |
| SAE-121 | Inférence test | **3pts** |
| SAE-122 | Nettoyage code | -3pts pénalités |

### ✅ Couvert par le cours uniquement — bonus (1 story)

| Story | Titre | Pts grille |
|-------|-------|:----------:|
| SAE-77 | Word2Vec training | 0pt (✅ Done) |

### ❌ Non requis — ni sujet, ni cours, ni grille (4 stories)

| Story | Titre | Justification |
|-------|-------|---------------|
| SAE-78 | Document embeddings | Travail complémentaire (✅ Done) |
| SAE-79 | Visualisation t-SNE | Travail complémentaire (✅ Done) |
| SAE-102 | Librairie partagée src/ | Bonne pratique (✅ Done) |
| SAE-123 | Tests pytest | Bonne pratique (⬜ Todo) |

---

## 4. Comprendre les blocs de points

### ML classiques (plusieurs) — 4pts

Pour obtenir les **4pts**, il faut faire du ML classique sur les **3 représentations** :

```
ML + N-grammes (SAE-116) ─── 1pt individuel
ML + TF-IDF   (SAE-114) ─── 1pt individuel    → Les 3 ensemble = 4pts "plusieurs"
ML + LLM      (SAE-117) ─── 1pt individuel
                              Total possible : 3 + 4 = 7pts
```

### Arch Deep (plusieurs) — 4pts

Pour obtenir les **4pts**, il faut faire du Deep Learning sur les **3 représentations** :

```
Deep + N-grammes (SAE-115) ─── 1pt individuel
Deep + TF-IDF    (SAE-113) ─── 1pt individuel    → Les 3 ensemble = 4pts "plusieurs"
Deep + LLM       (SAE-119) ─── 1pt individuel
                                Total possible : 3 + 4 = 7pts
```

### Inférence — 5pts

```
Modèle optimal  (SAE-120) ─── 2pts   (choisir le meilleur parmi tous les modèles)
Inférence test  (SAE-121) ─── 3pts   (appliquer sur données de test fournies)
                               Total : 5pts
```

---

## 5. Score total visé : 24/24

| Bloc | Pts | État |
|------|:---:|:----:|
| Préparation données | 1 | ✅ Acquis |
| Repr N-grammes + TF-IDF | 2 | ✅ Acquis |
| LLM embeddings | 1 | ⬜ Todo |
| Sélection variables | 1 | ⬜ Todo |
| ML classiques (3 repr × plusieurs algo) | 4+3 = 7 | ⬜ Todo |
| Deep Learning (3 repr × plusieurs arch) | 4+3 = 7 | ⬜ Todo |
| Inférence (optimal + test) | 2+3 = 5 | ⬜ Todo |
| Pénalités évitées | 0 | ⬜ Todo |
| **TOTAL** | **24** | **3/24 acquis** |

---

*Rapport généré le 20 février 2026. Sources : `sujet/Sujet S6 AGED 25-26.pdf`, `sujet/Cours Text Representation.pdf`, `sujet/IA Générative LLM Light.pdf`. Synchronisé avec Linear (équipe SAE6C01) et le dépôt GitHub adamelhirch/S6C01.*
