# Plan de Projet S6C01 - Analyse Yelp

**Dernière mise à jour:** 30 janvier 2026

## 🎯 Vue d'ensemble

Projet d'analyse du dataset Yelp Academic utilisant Python, NLP et Machine Learning.

**Durée estimée:** 8-10 semaines (27 jan - 28 fév 2026)
**Équipe:** 4 personnes
**Livrables:** Notebooks Jupyter + Rapport + Présentation

---

## 📋 Structure des Epics

### **Epic 1 - Setup & Data Loading** (27 jan - 31 jan)
**Objectif:** Configuration environnement + chargement et nettoyage des données JSON

#### Phase 1: Setup (SAE-58 à SAE-63)
- ✅ SAE-58: Configuration Python venv (1pt) - Urgent
- ✅ SAE-59: Installation dépendances (2pts) - Urgent
- ✅ SAE-60: Structure dossiers + .gitignore (2pts) - Urgent
- ✅ SAE-61: Configuration GitHub (3pts) - Urgent
- SAE-62: Configuration Linear ↔ GitHub (2pts) - Urgent
- SAE-63: Configuration Jupyter (2pts) - High

**Total Phase 1:** 12 points (~12-15h)

#### Phase 2: Chargement JSON (SAE-64 à SAE-66)
- SAE-64: Chargement Business JSON (2pts) - High
- SAE-65: Chargement Reviews JSON (2pts) - High
- SAE-66: Chargement Users JSON (2pts) - High

**Total Phase 2:** 6 points (~6h)

#### Phase 3: Nettoyage Données (SAE-96 à SAE-98)
- SAE-96: Nettoyage Business (3pts) - Urgent
- SAE-97: Nettoyage Reviews (3pts) - Urgent
- SAE-98: Nettoyage Users (2pts) - High

**Total Phase 3:** 8 points (~8h)

#### Phase 4: Analyses Exploratoires (SAE-67, 68, 95, 99-101)
- SAE-67: Dashboard Profils Reviewers (3pts) - High
- SAE-68: Dashboard Performance Établissements (3pts) - High
- SAE-95: Dashboard Analyse Sémantique (3pts) - High
- SAE-99: Analyse Temporelle (3pts) - High
- SAE-100: Analyse Géographique (3pts) - High
- SAE-101: Analyse Corrélations (2pts) - Urgent
- SAE-69: Échantillonnage (si nécessaire) (2pts) - Medium

**Total Phase 4:** 19 points (~19-22h)

**TOTAL EPIC 1:** 45 points (~45-50h pour l'équipe)

---

### **Epic 2 - Preprocessing & Text Cleaning** (1 fév - 5 fév)
**Objectif:** Preprocessing NLP des avis textuels

**Prérequis:** SAE-97 (Nettoyage Reviews) terminé

- SAE-70: Nettoyage Texte Basique (2pts) - Urgent
- SAE-71: Tokenization NLTK (2pts) - High
- SAE-72: Suppression Stopwords (2pts) - High
- SAE-73: Lemmatization (2pts) - High
- SAE-74: Pipeline Preprocessing Complet (3pts) - Urgent

**TOTAL EPIC 2:** 11 points (~11-13h)

---

### **Epic 3 - Text Representation** (6 fév - 12 fév)
**Objectif:** Représentation textuelle (TF-IDF, Word2Vec, embeddings)

**Prérequis:** Epic 2 terminé

- SAE-36: TF-IDF Vectorization (3pts)
- SAE-37: Analyse TF-IDF (mots importants) (2pts)
- SAE-38: Word2Vec Training (4pts)
- SAE-39: Visualisation Word Embeddings (3pts)
- SAE-40: Similarité sémantique (2pts)

**TOTAL EPIC 3:** 14 points (~14-16h)

---

### **Epic 4 - ML Classique & Analysis** (13 fév - 18 fév)
**Objectif:** Machine Learning classique (classification, clustering, recommandation)

**Prérequis:** Epic 3 terminé

#### Classification
- SAE-41: Préparation dataset classification (2pts)
- SAE-42: Logistic Regression baseline (2pts)
- SAE-43: Random Forest / SVM (3pts)
- SAE-44: Évaluation et comparaison modèles (2pts)

#### Clustering
- SAE-45: K-Means Clustering (3pts)
- SAE-46: Visualisation clusters (2pts)

#### Recommandation
- SAE-47: Système de recommandation basique (3pts)

**TOTAL EPIC 4:** 17 points (~17-20h)

---

### **Epic 5 - LLM Local (HuggingFace)** (19 fév - 24 fév)
**Objectif:** LLMs locaux avec HuggingFace (BERT, sentiment analysis)

**Prérequis:** Epic 4 terminé

- SAE-48: BERT Classification Sentiment (4pts)
- SAE-49: Génération Résumés (4pts)
- SAE-50: Fine-tuning BERT (optionnel) (6pts)
- SAE-51: Comparaison LLM vs ML Classique (3pts)

**TOTAL EPIC 5:** 17 points (~17-20h)

---

### **Epic 6 - Documentation & Rendu Final** (25 fév - 28 fév)
**Objectif:** Finalisation, visualisations, rapport et présentation

- SAE-52: Notebook Final Structuration (4pts)
- SAE-53: Visualisations Finales (3pts)
- SAE-54: Rapport Technique (5pts)
- SAE-55: README et Documentation Code (2pts)
- SAE-56: Préparation Présentation Orale (4pts)

**TOTAL EPIC 6:** 18 points (~18-20h)

---

## 📊 Récapitulatif Global

| Epic | Points | Heures estimées | Dates |
|------|--------|-----------------|-------|
| Epic 1 | 45 | 45-50h | 27 jan - 31 jan |
| Epic 2 | 11 | 11-13h | 1 fév - 5 fév |
| Epic 3 | 14 | 14-16h | 6 fév - 12 fév |
| Epic 4 | 17 | 17-20h | 13 fév - 18 fév |
| Epic 5 | 17 | 17-20h | 19 fév - 24 fév |
| Epic 6 | 18 | 18-20h | 25 fév - 28 fév |
| **TOTAL** | **122** | **122-139h** | **8 semaines** |

**Charge par personne:** ~30-35h (équipe de 4)

---

## ✅ Cohérence du Plan

### 1. **Dépendances respectées**
- ✅ Epic 1 → Epic 2 (données nettoyées → preprocessing)
- ✅ Epic 2 → Epic 3 (texte preprocessé → vectorisation)
- ✅ Epic 3 → Epic 4 (vecteurs → ML)
- ✅ Epic 4 → Epic 5 (baseline ML → comparaison LLM)
- ✅ Epic 5 → Epic 6 (analyses terminées → documentation)

### 2. **Progression logique**
```
Données brutes (JSON)
    ↓
Données nettoyées (Parquet)
    ↓
Texte preprocessé (tokenized, lemmatized)
    ↓
Représentations vectorielles (TF-IDF, Word2Vec)
    ↓
Modèles ML (Classification, Clustering)
    ↓
LLMs (BERT, HuggingFace)
    ↓
Documentation et présentation
```

### 3. **Outputs clairs**

**Epic 1:**
- `data/cleaned/business_clean.parquet`
- `data/cleaned/reviews_clean.parquet`
- `data/cleaned/users_clean.parquet`
- Dashboards d'analyse exploratoire

**Epic 2:**
- Colonne `text_preprocessed` dans reviews
- Fonction `preprocess_pipeline()` réutilisable

**Epic 3:**
- Matrices TF-IDF
- Modèles Word2Vec entraînés
- Visualisations embeddings

**Epic 4:**
- Modèles de classification entraînés
- Clusters identifiés
- Système de recommandation

**Epic 5:**
- Modèles BERT fine-tunés
- Résumés générés
- Comparaison performances

**Epic 6:**
- Notebook final complet
- Rapport PDF (5-10 pages)
- Présentation PowerPoint

### 4. **Analyses du sujet couvertes**

✅ **Dashboard 1 - Profils Reviewers** (SAE-67)
- Sévérité des experts
- Niveau de détail
- Segmentation reviewers

✅ **Dashboard 2 - Performance Établissements** (SAE-68)
- Répartition par catégorie
- Volume vs Note
- Impact visuel (photos)

✅ **Dashboard 3 - Analyse Sémantique** (SAE-95)
- Longueur vs Note
- Duel des mots (TF-IDF Word Clouds)
- Indice de satisfaction

✅ **Analyses complémentaires:**
- Temporelle (SAE-99)
- Géographique (SAE-100)
- Corrélations (SAE-101)

### 5. **Équilibrage de la charge**

**Epic 1 (45pts)** = Plus lourd car:
- Setup initial
- 3 datasets à nettoyer
- 6 dashboards/analyses

**Epics 2-5 (11-17pts chacun)** = Équilibrés
- Tâches techniques spécialisées
- Charge répartie sur les membres

**Epic 6 (18pts)** = Finalisation
- Documentation
- Polissage
- Préparation présentation

---

## 🚨 Points d'attention

### Risques identifiés

1. **Epic 1 très chargé (45pts)**
   - **Mitigation:** Paralléliser les tâches entre membres de l'équipe
   - Setup (SAE-58-63): Personne A
   - Chargement (SAE-64-66): Personne B
   - Nettoyage (SAE-96-98): Personne C
   - Dashboards (SAE-67-68-95): Personne D

2. **Dépendances strictes**
   - **Mitigation:** Ne pas commencer un Epic avant que le précédent soit validé
   - Checkpoint après chaque Epic

3. **Taille du dataset**
   - **Mitigation:** SAE-69 (Échantillonnage) disponible si nécessaire
   - Tester sur petit échantillon d'abord

4. **Temps pour LLMs (Epic 5)**
   - **Mitigation:** Fine-tuning optionnel (SAE-50)
   - Priorité sur BERT classification et génération résumés

---

## 📝 Recommandations

### Pour Epic 1 (urgent)

**Priorité 1 (Cette semaine):**
1. SAE-58, 59, 60, 61 → Setup complet ✅
2. SAE-62 → Intégration Linear ↔ GitHub
3. SAE-64, 65, 66 → Chargement des 3 fichiers JSON
4. SAE-96, 97, 98 → Nettoyage des données

**Priorité 2 (Semaine prochaine):**
5. SAE-67, 68, 95 → Les 3 dashboards principaux
6. SAE-101 → Analyse corrélations
7. SAE-99, 100 → Analyses temporelles/géo (si temps)

### Organisation équipe

**Semaine 1 (Epic 1):**
- **Personne A:** Setup + Linear (SAE-58-62)
- **Personne B:** Chargement Business + Users (SAE-64, 66)
- **Personne C:** Chargement Reviews + Nettoyage (SAE-65, 97)
- **Personne D:** Nettoyage Business + Users (SAE-96, 98)

**Semaine 2 (Epic 1 fin + Epic 2 début):**
- **Tous:** Dashboards en parallèle (SAE-67, 68, 95)
- **Personne A + B:** Epic 2 (Preprocessing)

---

## 🎯 Jalons (Milestones)

- **31 jan:** Epic 1 terminé ✅ Données chargées et nettoyées
- **5 fév:** Epic 2 terminé ✅ Texte preprocessé
- **12 fév:** Epic 3 terminé ✅ Représentations vectorielles
- **18 fév:** Epic 4 terminé ✅ Modèles ML
- **24 fév:** Epic 5 terminé ✅ LLMs testés
- **28 fév:** Epic 6 terminé ✅ Rendu final

---

**Conclusion:** Le plan est cohérent, les dépendances sont claires, et les charges sont équilibrées. Epic 1 est le plus critique et doit être priorisé dès maintenant.
