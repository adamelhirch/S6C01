# 📋 Récapitulatif des Epics & Stories - Projet S6C01 Yelp Analysis

**Projet:** S6C01 - Analyse Dataset Yelp Academic
**Équipe:** Adam (chef de projet), Ewen, Natalia, Manolo, Lotfi
**Période:** 27 janvier - 28 février 2026
**Linear:** https://linear.app/sae6c01

---

## 📊 Vue d'ensemble

| Epic | Dates | Stories | Points | Status |
|------|-------|---------|--------|--------|
| Epic 1 - Setup & Data Loading | 27-31 jan | 13 | 27 | Backlog |
| Epic 2 - Preprocessing & Text Cleaning | 1-5 fév | 5 | 11 | Backlog |
| Epic 3 - Text Representation | 6-12 fév | 6 | 18 | Backlog |
| Epic 4 - ML Classique & Analysis | 13-18 fév | 5 | 20 | Backlog |
| Epic 5 - LLM Local (HuggingFace) | 19-24 fév | 4 | 13 | Backlog |
| Epic 6 - Documentation & Rendu Final | 25-28 fév | 5 | 19 | Backlog |
| **TOTAL** | **1 mois** | **38** | **108** | - |

**Répartition équitable:** 108 points ÷ 5 personnes = **~21-22 points par personne**

---

## 🚀 Epic 1 - Setup & Data Loading

**📅 Dates:** 27-31 janvier 2026
**🎯 Objectif:** Configuration de l'environnement Python, chargement des données Yelp et analyse exploratoire initiale
**📊 Stories:** 13 | **Points:** 27

### Stories Epic 1

| ID | Titre | Points | Priorité | Dépendances |
|----|-------|--------|----------|-------------|
| **SAE-58** | Configuration Environnement Python + venv | 1 | 🔴 Urgent | - |
| **SAE-59** | Installation des dépendances Python | 2 | 🔴 Urgent | SAE-58 |
| **SAE-60** | Structure de dossiers et .gitignore | 2 | 🔴 Urgent | - |
| **SAE-61** | Configuration GitHub Repository | 3 | 🔴 Urgent | SAE-60 |
| **SAE-62** | Configuration Linear + Intégration GitHub | 2 | 🔴 Urgent | SAE-61 |
| **SAE-63** | Configuration Jupyter + Extensions | 2 | 🟡 High | SAE-58, SAE-59 |
| **SAE-64** | Chargement données Business JSON | 2 | 🟡 High | SAE-60, SAE-63 |
| **SAE-65** | Chargement données Reviews JSON | 2 | 🟡 High | SAE-60, SAE-63 |
| **SAE-66** | Chargement données Users JSON | 2 | 🟢 Medium | SAE-65 |
| **SAE-67** | EDA - Analyse Exploratoire Business | 3 | 🟡 High | SAE-64 |
| **SAE-68** | EDA - Analyse Exploratoire Reviews | 3 | 🟡 High | SAE-65 |
| **SAE-69** | Échantillonnage Dataset (si trop gros) | 2 | 🟢 Medium | SAE-65 |
| **SAE-95** | EDA - Analyse Exploratoire Users | 3 | 🟡 High | SAE-66 |

**⚠️ Stories bloquantes à faire EN PREMIER:**
- SAE-61 (GitHub repo) - 3 points
- SAE-62 (Linear + GitHub) - 2 points

---

## 🧹 Epic 2 - Preprocessing & Text Cleaning

**📅 Dates:** 1-5 février 2026
**🎯 Objectif:** Nettoyage et préparation du texte pour l'analyse NLP
**📊 Stories:** 5 | **Points:** 11

### Stories Epic 2

| ID | Titre | Points | Priorité | Dépendances |
|----|-------|--------|----------|-------------|
| **SAE-70** | Nettoyage de texte (lowercase, ponctuation, etc.) | 2 | 🟡 High | SAE-65 |
| **SAE-71** | Tokenization avec NLTK/spaCy | 2 | 🟡 High | SAE-70 |
| **SAE-72** | Suppression des stopwords | 1 | 🟡 High | SAE-71 |
| **SAE-73** | Lemmatization / Stemming | 3 | 🟡 High | SAE-72 |
| **SAE-74** | Pipeline de preprocessing réutilisable | 3 | 🟡 High | SAE-73 |

**Livrables:**
- Texte nettoyé et tokenisé
- Pipeline preprocessing dans `src/preprocessing.py`
- Notebook de démonstration

---

## 📝 Epic 3 - Text Representation

**📅 Dates:** 6-12 février 2026
**🎯 Objectif:** Techniques de représentation textuelle (TF-IDF, Word2Vec, embeddings, visualisations)
**📊 Stories:** 6 | **Points:** 18

### Stories Epic 3

| ID | Titre | Points | Priorité | Dépendances |
|----|-------|--------|----------|-------------|
| **SAE-75** | TF-IDF - Vectorisation basique | 2 | 🟡 High | SAE-74 |
| **SAE-76** | TF-IDF - Optimisation et features importantes | 3 | 🟡 High | SAE-75 |
| **SAE-77** | Word2Vec avec Gensim | 3 | 🟡 High | SAE-74 |
| **SAE-78** | Embeddings et similarité sémantique | 3 | 🟢 Medium | SAE-77 |
| **SAE-79** | Visualisation t-SNE des embeddings | 3 | 🟢 Medium | SAE-77, SAE-78 |
| **SAE-80** | Analyse de fréquence et n-grams | 2 | 🟢 Medium | SAE-74 |

**Livrables:**
- Matrices TF-IDF sauvegardées
- Modèle Word2Vec entraîné
- Visualisations t-SNE
- Notebook comparatif TF-IDF vs Word2Vec

---

## 🤖 Epic 4 - ML Classique & Analysis

**📅 Dates:** 13-18 février 2026
**🎯 Objectif:** Modèles de Machine Learning classiques (classification, clustering, recommandation)
**📊 Stories:** 5 | **Points:** 20

### Stories Epic 4

| ID | Titre | Points | Priorité | Dépendances |
|----|-------|--------|----------|-------------|
| **SAE-81** | Classification - Logistic Regression baseline | 3 | 🟡 High | SAE-75 ou SAE-77 |
| **SAE-82** | Classification - Comparaison modèles (SVM, RF, NB) | 5 | 🟡 High | SAE-81 |
| **SAE-83** | Clustering - K-Means sur embeddings | 3 | 🟡 High | SAE-77 |
| **SAE-84** | Analyse statistique et feature importance | 3 | 🟢 Medium | SAE-82 |
| **SAE-85** | Système de recommandation simple | 5 | 🟢 Medium | SAE-78, SAE-83 |

**Objectif de performance:**
- Accuracy baseline: ~70-75%
- Meilleur modèle: ~80-85%
- Comparaison TF-IDF vs Word2Vec

**Livrables:**
- Modèles entraînés (`.pkl`)
- Classification reports
- Notebook comparatif
- Matrice de confusion et métriques

---

## 🧠 Epic 5 - LLM Local (HuggingFace)

**📅 Dates:** 19-24 février 2026
**🎯 Objectif:** LLMs locaux gratuits avec HuggingFace (BERT, sentiment analysis, génération)
**📊 Stories:** 4 | **Points:** 13

### Stories Epic 5

| ID | Titre | Points | Priorité | Dépendances |
|----|-------|--------|----------|-------------|
| **SAE-86** | Setup HuggingFace Transformers (local) | 2 | 🟡 High | SAE-74 |
| **SAE-87** | BERT fine-tuning pour sentiment analysis | 5 | 🟡 High | SAE-86 |
| **SAE-88** | Génération de résumés avec LLM local | 3 | 🟢 Medium | SAE-86 |
| **SAE-89** | Comparaison LLM vs ML classique | 3 | 🟡 High | SAE-82, SAE-87 |

**⚠️ Contrainte CRITIQUE:** UNIQUEMENT modèles GRATUITS et LOCAUX
- ✅ HuggingFace: BERT, DistilBERT, RoBERTa
- ❌ OpenAI, Claude API, Cohere (INTERDITS - payants)

**Livrables:**
- Modèle BERT fine-tuned
- Comparaison performances LLM vs ML
- Analyse coût computationnel
- Notebook démonstration

---

## 📊 Epic 6 - Documentation & Rendu Final

**📅 Dates:** 25-28 février 2026
**🎯 Objectif:** Visualisations finales, rapport technique et présentation orale
**📊 Stories:** 5 | **Points:** 19

### Stories Epic 6

| ID | Titre | Points | Priorité | Dépendances |
|----|-------|--------|----------|-------------|
| **SAE-90** | Notebook final intégré (toutes les étapes) | 5 | 🔴 Urgent | Tous les Epics |
| **SAE-91** | README.md complet et professionnel | 2 | 🔴 Urgent | SAE-90 |
| **SAE-92** | Rapport technique PDF (15-20 pages) | 5 | 🔴 Urgent | SAE-90 |
| **SAE-93** | Présentation orale PowerPoint/PDF | 3 | 🔴 Urgent | SAE-92 |
| **SAE-94** | Dashboard de visualisations interactives | 3 | 🟢 Medium | SAE-90 |

**Contenu rapport technique:**
1. Introduction & problématique
2. État de l'art (Text Representation, ML, LLM)
3. Méthodologie (preprocessing, features, modèles)
4. Résultats expérimentaux (métriques, comparaisons)
5. Discussion et limites
6. Conclusion et perspectives

**Livrables:**
- `FINAL-notebook.ipynb` exécutable end-to-end
- `README.md` avec instructions complètes
- `docs/rapport-technique.pdf`
- `docs/presentation.pptx`
- Dashboard Plotly (optionnel)

---

## 📈 Distribution recommandée par membre

**Principe:** ~21-22 points par personne, selon compétences

### Option 1 - Par Epic

```
Adam (chef projet):
- Epic 1: SAE-61, SAE-62 (5 pts) - Setup GitHub/Linear
- Epic 6: SAE-90, SAE-91, SAE-92 (12 pts) - Coordination rendu final
- Epic 3: SAE-75 (2 pts) - TF-IDF basique
- TOTAL: 19 points

Ewen:
- Epic 1: SAE-58, SAE-59, SAE-60, SAE-63 (7 pts) - Setup technique
- Epic 2: SAE-70, SAE-71, SAE-72 (5 pts) - Preprocessing
- Epic 3: SAE-80 (2 pts) - N-grams
- Epic 6: SAE-93 (3 pts) - Présentation
- TOTAL: 17 points → ajouter SAE-94 (3 pts) = 20 points

Natalia:
- Epic 1: SAE-64, SAE-67 (5 pts) - Business data
- Epic 3: SAE-76, SAE-77 (6 pts) - TF-IDF optimisé + Word2Vec
- Epic 4: SAE-81, SAE-84 (6 pts) - Logistic Regression + stats
- TOTAL: 17 points → ajouter SAE-69 (2 pts) + SAE-94 partiel = 19-22 points

Manolo:
- Epic 1: SAE-65, SAE-68 (5 pts) - Reviews data
- Epic 2: SAE-73, SAE-74 (6 pts) - Lemma + pipeline
- Epic 4: SAE-82 (5 pts) - Comparaison modèles ML
- TOTAL: 16 points → ajouter SAE-78 (3 pts) + SAE-85 partiel = 19-22 points

Lotfi:
- Epic 1: SAE-66, SAE-95 (5 pts) - Users data + EDA
- Epic 3: SAE-78, SAE-79 (6 pts) - Embeddings + t-SNE
- Epic 4: SAE-83, SAE-85 (8 pts) - Clustering + recommandation
- Epic 5: SAE-86, SAE-87 (7 pts) - LLM setup + BERT
- TOTAL: 26 points → retirer SAE-85 partiel ou autres = 21-22 points
```

**⚠️ IMPORTANT:** Cette distribution est une SUGGESTION. Ajustez selon:
- Les compétences de chacun
- La charge de travail réelle
- Les imprévus
- L'entraide entre membres

---

## 🔄 Workflow de travail

### 1. Avant de commencer une story

```bash
☐ Ouvrir Linear
☐ S'assigner la story
☐ Passer en "In Progress"
☐ Lire TOUTE la description + critères
☐ Vérifier les dépendances
```

### 2. Pendant le développement

```bash
# Créer une branche
git checkout -b SAE-XX-description

# Coder, committer régulièrement
git commit -m "SAE-XX: Description"

# Commenter dans Linear toutes les 2h
```

### 3. Finalisation

```bash
# Push + PR
git push origin SAE-XX-description

# Review par un autre membre
# Merger après approbation

# Marquer "Done" dans Linear
```

---

## 🎯 Prochaines actions

### Cette semaine (27-31 janvier) - Epic 1

**URGENT - À faire EN PREMIER:**
1. SAE-61: Créer le repo GitHub (Adam)
2. SAE-62: Intégration Linear + GitHub (Adam)

**Parallèle:**
3. SAE-58, SAE-59, SAE-60: Setup Python (Ewen)
4. SAE-63: Jupyter (Ewen ou Natalia)

**Ensuite:**
5. SAE-64, SAE-65, SAE-66: Load data (Natalia, Manolo, Lotfi)
6. SAE-67, SAE-68, SAE-95: EDA (répartir entre 3 personnes)
7. SAE-69: Échantillonnage (si nécessaire)

---

## 📊 Suivi de progression

**Actuellement:**
- ✅ Linear configuré avec 6 Epics
- ✅ 38 stories créées
- ✅ Guides de collaboration créés
- ✅ Config Claude préparée
- ⏳ **À faire:** Kickoff meeting + distribution des tâches

**Objectif fin janvier:**
- Epic 1 100% Done (27 points)
- Environnement prêt
- Données chargées et explorées
- Prêt pour Epic 2 (preprocessing)

**Objectif mi-février:**
- Epics 2, 3, 4 terminés
- Modèles ML entraînés
- Baseline établie

**Objectif fin février:**
- Epic 5 terminé (LLM)
- Epic 6 terminé (rendu)
- Projet livré ✅

---

## 🆘 En cas de problème

1. **Bloqué sur une story?**
   - Commenter dans Linear avec @mention
   - Demander aide Discord/WhatsApp
   - "Claude, aide-moi sur SAE-XX"

2. **En retard?**
   - Réunion d'urgence
   - Reprioriser les stories
   - Paralléliser si possible

3. **Conflit Git?**
   - Voir `GUIDE-COLLABORATION.md`
   - Demander à Adam

---

**Dernière mise à jour:** 27 janvier 2026
**Version:** 1.0
**Auteur:** Adam + Claude

**LET'S GO TEAM! 🚀**
