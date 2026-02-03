# 🤖 PROJECT CONTEXT - S6C01 Yelp Analysis

**Pour Claude Code et autres assistants IA**

Ce document fournit le contexte complet du projet pour une compréhension immédiate et une assistance optimale.

---

## 🚀 QUICK START pour les IA

**Tu as accès aux MCP servers Linear et GitHub.** Voici les actions automatiques à effectuer:

### 1. Quand l'utilisateur commence une story:
- Créer la branche Git avec le bon format
- **AUTOMATIQUEMENT** ajouter le lien de branche dans Linear avec `mcp__linear-server__update_issue`
- Mettre la story en "In Progress"

### 2. Quand l'utilisateur termine une story:
- **AUTOMATIQUEMENT** créer la PR avec `mcp__github__create_pull_request`
- **AUTOMATIQUEMENT** ajouter le lien de PR dans Linear (EN PLUS du lien de branche)
- **AUTOMATIQUEMENT** mettre la story en "In Review"
- Informer l'utilisateur que c'est prêt pour review

### 3. Format des liens Linear:
- **Branche**: `"title": "Branche GitHub: {nom-branche}", "url": "https://github.com/adamelhirch/S6C01/tree/{nom-branche}"`
- **PR**: `"title": "PR #{num}: {titre}", "url": "https://github.com/adamelhirch/S6C01/pull/{num}"`

**⚠️ IMPORTANT:** Toujours AJOUTER aux liens existants, JAMAIS les remplacer!

---

## 📋 Vue d'ensemble

**Type**: Projet académique de Data Science / Machine Learning / NLP
**Niveau**: BUT Informatique - Semestre 6 (2025-2026)
**Dataset**: Yelp Academic Dataset (Business, Reviews, Users)
**Méthodologie**: Agile (Scrum) avec Linear pour le tracking

---

## 🎯 Structure du projet (Epics → Stories → Tasks)

### Hiérarchie

```
Epic (Initiative/Project)
  └── Stories (Issues)
      └── Tasks (Checklist dans la description)
```

**Le projet est divisé en 6 Epics:**

1. **Epic 1**: Setup + Chargement et nettoyage des données JSON
2. **Epic 2**: Preprocessing & Text Cleaning (NLP)
3. **Epic 3**: Text Representation (TF-IDF, Word2Vec, Embeddings)
4. **Epic 4**: ML Classique (Classification, Clustering, Recommandation)
5. **Epic 5**: LLM Local (BERT, HuggingFace)
6. **Epic 6**: Documentation & Rendu Final

### Stories

**Chaque story (SAE-XX):**
- Appartient à une Epic (projet/initiative dans Linear)
- Contient une **checklist de tâches** dans sa description
- A des critères d'acceptation clairs
- Est trackée dans `docs/PROJECT-PLAN.md`

### Tasks

**Les tâches dans une story sont des checkbox dans la description:**
```markdown
## Tasks
- [ ] Tâche 1
- [ ] Tâche 2
- [x] Tâche 3 (complétée)
```

**IMPORTANT:** Cocher les tâches au fur et à mesure dans Linear quand tu les complètes.

---

## 🛠️ Stack Technologique

### Langage & Environnement
- **Python**: 3.12+ (obligatoire)
- **Environnement**: `venv` (environnement virtuel Python)
- **IDE**: Jupyter Notebook pour l'exploration et l'analyse

### Bibliothèques principales

**Data Manipulation**
- `pandas` >= 2.1.4 - DataFrames et manipulation de données
- `numpy` >= 1.26.2 - Calcul numérique
- `pyarrow` >= 14.0.1 - Support Parquet (format optimisé)

**Data Visualization**
- `matplotlib` >= 3.8.2 - Graphiques de base
- `seaborn` >= 0.13.0 - Visualisations statistiques
- `plotly` >= 5.18.0 - Graphiques interactifs

**NLP & Text Processing**
- `nltk` >= 3.8.1 - Preprocessing NLP (tokenization, stopwords, stemming)
- `wordcloud` >= 1.9.3 - Nuages de mots
- `langdetect` >= 1.0.9 - Détection de langue

**Machine Learning**
- `scikit-learn` >= 1.3.2 - ML classique (classification, clustering, TF-IDF)
- `scipy` >= 1.12.0 - Fonctions scientifiques

**LLM & Deep Learning**
- `transformers` >= 4.36.2 - HuggingFace (BERT, etc.)
- `torch` >= 2.2.0 - PyTorch (backend pour Transformers)
- `sentencepiece` >= 0.1.99 - Tokenization pour LLM

**Jupyter**
- `jupyter` >= 1.0.0 - Interface Jupyter
- `notebook` >= 7.0.6 - Jupyter Notebook
- `ipywidgets` >= 8.1.1 - Widgets interactifs

**Utilities**
- `tqdm` >= 4.66.1 - Progress bars
- `python-dateutil` >= 2.8.2 - Manipulation de dates

---

## 📁 Structure du Projet

```
S6C01/
├── README.md                   # Documentation principale
├── requirements.txt            # Dépendances Python
├── .gitignore                 # Fichiers exclus de Git
│
├── .agent/                    # Configuration Antigravity
│   └── workflows/             # Workflows pour Antigravity
│       ├── setup-environment.md
│       ├── start-development.md
│       ├── run-jupyter.md
│       └── data-pipeline.md
│
├── .claude/                   # Configuration Claude Code
│   ├── PROJECT_CONTEXT.md     # Ce fichier
│   ├── settings.local.json    # Permissions
│   └── commands/              # Commandes préconfigurées
│
├── data/                      # Données (NON versionnées sur Git)
│   ├── raw/                   # JSON bruts Yelp (~6 GB)
│   │   ├── yelp_academic_dataset_business.json          (~120 MB)
│   │   ├── yelp_academic_reviews4students.jsonl         (~5 GB)
│   │   └── yelp_academic_dataset_user4students.jsonl    (~600 MB)
│   └── cleaned/               # Données nettoyées (Parquet)
│       ├── business_clean.parquet
│       ├── reviews_clean.parquet
│       └── users_clean.parquet
│
├── notebooks/                 # Jupyter notebooks (exploration)
│   ├── 01_data_loading.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_preprocessing.ipynb
│   └── ...
│
├── src/                       # Code source Python (réutilisable)
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── preprocessing.py
│   └── ...
│
├── outputs/                   # Visualisations et rapports
│   ├── figures/
│   └── reports/
│
└── docs/                      # Documentation
    ├── QUICKSTART.md          # Guide démarrage rapide
    ├── AI_INSTRUCTIONS.md     # Instructions pour IA
    └── stories/               # Documentation par story
```

---

## 🔄 Architecture des Données

### Pipeline de Traitement

```
data/raw/*.json → notebooks/0X_*.ipynb → data/cleaned/*.parquet → outputs/
```

1. **Chargement** (`01_data_loading.ipynb`): JSON → Pandas DataFrame
2. **Nettoyage** (`02_data_cleaning.ipynb`): Doublons, NaN, text cleaning
3. **Preprocessing** (`03_preprocessing.ipynb`): Tokenization, stopwords, lemmatization
4. **Analyse** (`04_eda_dashboards.ipynb`): Exploration et visualisations
5. **Modeling** (`05+`): TF-IDF, Word2Vec, Classification, etc.

### Datasets Yelp

**Business** (~150k commerces)
- Restaurants, bars, hôtels, etc.
- Colonnes clés: `business_id`, `name`, `city`, `state`, `stars`, `categories`

**Reviews** (~6M avis)
- Textes d'avis clients
- Colonnes clés: `review_id`, `user_id`, `business_id`, `stars`, `text`, `date`

**Users** (~2M utilisateurs)
- Profils utilisateurs Yelp
- Colonnes clés: `user_id`, `name`, `review_count`, `average_stars`

---

## 🔄 Workflow Git + Linear

### Méthodologie

Le projet utilise **Linear** pour le tracking Agile et **GitHub** pour le versioning.

**Linear**: https://linear.app/sae6c01
**GitHub**: https://github.com/adamelhirch/S6C01

### Intégration Linear-GitHub (AUTOMATIQUE)

**Règle principale**: Toute story Linear DOIT avoir des liens vers sa branche ET sa PR GitHub dans ses ressources.

**Workflow automatisé quand une story est terminée:**

1. **Créer la Pull Request** automatiquement vers `main`
2. **Ajouter le lien de la PR** aux ressources de la story (en PLUS du lien de branche existant)
3. **Mettre la story en état "In Review"** dans Linear
4. Review et merge restent manuels (utilisateur ou coéquipiers)

#### Étape par étape pour l'IA:

**1. Après création d'une branche:**
```bash
git checkout -b prenom/sae-XX-description
git push -u origin prenom/sae-XX-description
```

Utiliser `mcp__linear-server__update_issue` pour ajouter le lien:
```json
{
  "id": "ISSUE_ID",
  "links": [{
    "title": "Branche GitHub: prenom/sae-XX-description",
    "url": "https://github.com/adamelhirch/S6C01/tree/prenom/sae-XX-description"
  }]
}
```

**2. Quand la story est terminée (code complet):**

a) Créer la PR avec `mcp__github__create_pull_request`:
```json
{
  "owner": "adamelhirch",
  "repo": "S6C01",
  "title": "SAE-XX: Titre de la story",
  "head": "prenom/sae-XX-description",
  "base": "main",
  "body": "Description de la PR\n\nCloses SAE-XX"
}
```

b) AJOUTER le lien PR (SANS supprimer le lien branche):
```json
{
  "id": "ISSUE_ID",
  "links": [
    {
      "title": "Branche GitHub: prenom/sae-XX-description",
      "url": "https://github.com/adamelhirch/S6C01/tree/prenom/sae-XX-description"
    },
    {
      "title": "PR #XX: Titre de la PR",
      "url": "https://github.com/adamelhirch/S6C01/pull/XX"
    }
  ]
}
```

c) Mettre la story en "In Review":
```json
{
  "id": "ISSUE_ID",
  "state": "In Review"
}
```

**3. Story pour code déjà existant:**
- Attacher le lien de branche existante
- Si une PR existe déjà, ajouter aussi son lien
- Marquer "Done" si le code est mergé

### Workflow Complet

**1. Prendre une story sur Linear**
   - Utiliser `mcp__linear-server__list_issues` pour voir les stories disponibles
   - Ou demander à l'utilisateur quelle story il veut prendre
   - Mettre à jour la story en "In Progress" avec `mcp__linear-server__update_issue`

**2. Créer une branche Git**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b prenom/sae-XX-description
   ```
   Format: `prenom/sae-XX-description-courte`

   Exemples: `adam/sae-68-shared-lib`, `natalia/sae-72-tfidf`

   **Immédiatement après**, ajouter le lien de branche dans Linear (voir section Intégration ci-dessus)

**3. Développer**
   - Modifier notebooks (`notebooks/XX_description.ipynb`) ou code source (`src/`)
   - Tester localement
   - Si notebook: `Cell → All Output → Clear` avant de commiter

**4. Commiter**
   ```bash
   git add .
   git commit -m "SAE-XX Description courte

   - Détail 1
   - Détail 2
   - Détail 3

   Co-Authored-By: Claude (gemini-claude-sonnet-4-5-thinking) <noreply@anthropic.com>"
   ```

**5. Pousser**
   ```bash
   git push origin prenom/sae-XX-description
   ```

**6. Quand le développement est terminé:**
   - Créer automatiquement la PR (voir section Intégration)
   - Ajouter le lien PR dans Linear
   - Mettre la story en "In Review"
   - Informer l'utilisateur que la PR est prête pour review

**7. Review et Merge** (manuel par utilisateur)
   - L'utilisateur ou ses coéquipiers reviewent
   - Soit ils mergent manuellement
   - Soit ils demandent à l'IA de merger (avec `mcp__github__merge_pull_request`)
   - Après merge: mettre story en "Done" dans Linear

---

## 👥 Équipe

- **Adam EL HIRCH** - [@adamelhirch](https://github.com/adamelhirch)
- **Natalia ROS** - [@rsnataliaa](https://github.com/rsnataliaa)
- **Ewen MONTOUT** - [@ewen-montout](https://github.com/ewen-montout)
- **Manolo BRACH** - [@reyyko](https://github.com/reyyko)
- **Lotfi MELOUANE** - [@lotfimln](https://github.com/lotfimln)

---

## 🤖 Instructions Spéciales pour les IA

### Outils MCP Disponibles

**Linear MCP Server** (`mcp__linear-server__*`)
- `list_issues`: Lister les stories
- `get_issue`: Récupérer détails d'une story
- `update_issue`: Mettre à jour une story (state, links, etc.)
- `create_issue`: Créer une nouvelle story

**GitHub MCP Server** (`mcp__github__*`)
- `create_pull_request`: Créer une PR
- `list_pull_requests`: Lister les PRs
- `pull_request_read`: Lire les détails d'une PR
- `merge_pull_request`: Merger une PR
- `create_or_update_file`: Créer/modifier un fichier
- `push_files`: Pousser plusieurs fichiers en un commit

### Workflow Automatique Recommandé

Quand l'utilisateur dit "termine la story SAE-XX" ou similaire:

1. **Vérifier que tout est prêt:**
   - Code écrit et testé
   - Commits effectués
   - Branche poussée

2. **Créer la PR automatiquement:**
   - Utiliser `mcp__github__create_pull_request`
   - Titre: "SAE-XX: Description de la story"
   - Corps: Description + "Closes SAE-XX"

3. **Mettre à jour Linear automatiquement:**
   - Récupérer l'URL de la PR créée
   - Ajouter le lien aux ressources de la story (GARDER le lien de branche)
   - Mettre state à "In Review"

4. **Informer l'utilisateur:**
   - PR créée: [lien]
   - Story mise en review dans Linear
   - En attente de review par l'équipe

### Quand créer des liens Linear

- **Après chaque `git push` d'une nouvelle branche**: Ajouter lien branche
- **Après création de PR**: Ajouter lien PR (en PLUS de branche)
- **Jamais supprimer** les liens existants, seulement ajouter

### Format des repos et URLs

- **Repo GitHub**: `adamelhirch/S6C01`
- **Branche par défaut**: `main`
- **Format branche**: `prenom/sae-XX-description`
- **URL branche**: `https://github.com/adamelhirch/S6C01/tree/{nom-branche}`
- **URL PR**: `https://github.com/adamelhirch/S6C01/pull/{numero}`

### États Linear

- **Todo/Backlog**: Story pas commencée
- **In Progress**: En cours de développement
- **In Review**: PR créée, en attente de review
- **Done**: PR mergée

---

## ⚠️ Points Importants pour les IA

### 🚨 CRITIQUES

1. **Les fichiers JSON ne sont PAS versionnés**
   - Ils sont trop volumineux (~6 GB total)
   - Ils DOIVENT être dans `.gitignore`
   - Chaque membre doit les télécharger manuellement

2. **Toujours utiliser un environnement virtuel**
   ```bash
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Nomenclature des branches**
   - Format: `prenom/sae-XX-description`
   - JAMAIS de commits directs sur `main`

4. **Messages de commit**
   - TOUJOURS commencer par `SAE-XX`
   - Inclure `Co-Authored-By: Claude` si assisté par IA
   - Exemple:
     ```
     SAE-64 Add data cleaning pipeline

     - Remove duplicates
     - Handle missing values
     - Clean text data

     Co-Authored-By: Claude (gemini-claude-sonnet-4-5-thinking) <noreply@anthropic.com>
     ```

5. **Intégration Linear ↔ GitHub**
   - AUTOMATIQUEMENT ajouter liens de branche dans Linear après création
   - AUTOMATIQUEMENT créer PR et ajouter lien PR quand story terminée
   - AUTOMATIQUEMENT mettre story en "In Review" après création PR
   - Ne JAMAIS supprimer les liens existants, seulement en ajouter

### 📝 Conventions de Code

**Notebooks**
- Nomenclature: `XX_description.ipynb` (ex: `05_tfidf_analysis.ipynb`)
- Première cellule: Header avec Epic, Story, Auteur, Date
- Dernière action avant commit: `Cell → All Output → Clear`

**Code Python** (dans `src/`)
- PEP 8 (style Python standard)
- Docstrings pour toutes les fonctions
- Type hints recommandés

**Imports standard** (dans notebooks):
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# Configuration
pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8-darkgrid')
```

---

## 🚀 Commandes Courantes

### Setup Initial
```bash
# Créer venv
python3 -m venv venv

# Activer venv
source venv/bin/activate

# Installer dépendances
pip install -r requirements.txt

# Télécharger ressources NLTK
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### Développement
```bash
# Activer venv
source venv/bin/activate

# Lancer Jupyter
jupyter notebook

# Charger données (dans notebook)
df = pd.read_parquet('data/cleaned/reviews_clean.parquet')
```

### Git
```bash
# Créer branche
git checkout -b prenom/sae-XX-description

# Commiter
git add .
git commit -m "SAE-XX Description"

# Pousser
git push origin prenom/sae-XX-description
```

---

## 🎓 Ressources Utiles

- **Yelp Dataset Docs**: https://www.yelp.com/dataset/documentation/main
- **Pandas Docs**: https://pandas.pydata.org/docs/
- **Scikit-learn Docs**: https://scikit-learn.org/stable/
- **HuggingFace Docs**: https://huggingface.co/docs/transformers/
- **NLTK Book**: https://www.nltk.org/book/

---

## 💡 Pour bien assister l'équipe

### Synchronisation PROJECT-PLAN.md

**IMPORTANT:** Le fichier `docs/PROJECT-PLAN.md` doit rester synchronisé avec Linear.

**Quand mettre à jour PROJECT-PLAN.md:**
- Une story est complétée → Ajouter ✅ dans le plan
- Une story change d'état → Mettre à jour le statut
- Une nouvelle Epic commence → Documenter dans le plan
- Des stories sont ajoutées/modifiées → Refléter les changements

**Format dans PROJECT-PLAN.md:**
```markdown
### Epic X - Titre

#### Phase Y: Nom de la phase (SAE-XX à SAE-YY)
- ✅ SAE-XX: Description (Xpts) - État
- 🔄 SAE-YY: Description (Ypts) - In Progress
- ⏸️ SAE-ZZ: Description (Zpts) - Backlog
```

### Reconnaissance de tâches courantes

**"Je veux travailler sur SAE-XX"**
→ Lister les détails de la story avec `mcp__linear-server__get_issue`
→ Afficher la checklist de tâches
→ Créer la branche avec le bon format
→ Ajouter le lien de branche dans Linear

**"J'ai terminé [tâche]"**
→ Mettre à jour la description de la story pour cocher la checkbox
→ Utiliser `mcp__linear-server__update_issue` avec description mise à jour

**"Termine la story"** ou **"Crée la PR"**
→ Vérifier que toutes les tâches sont cochées
→ Vérifier que le code est commité et poussé
→ Créer la PR avec `mcp__github__create_pull_request`
→ Ajouter le lien PR dans Linear (en plus de la branche)
→ Mettre la story en "In Review"

**"Merge la PR"** (après approbation)
→ Utiliser `mcp__github__merge_pull_request`
→ Mettre la story en "Done" dans Linear
→ Mettre à jour `docs/PROJECT-PLAN.md` avec ✅

**"Quelles stories sont disponibles?"**
→ Utiliser `mcp__linear-server__list_issues` avec filtres appropriés
→ Filtrer par Epic si contexte donné

**"Mets à jour le plan"**
→ Lire Linear pour obtenir l'état actuel des stories
→ Mettre à jour `docs/PROJECT-PLAN.md` en conséquence

### Quand un membre demande de l'aide:

1. **Vérifier le contexte**:
   - Quelle Epic/Story ? (SAE-XX)
   - Quel notebook ?
   - Quel objectif ?

2. **Respecter la structure**:
   - Notebook pour exploration → `notebooks/`
   - Code réutilisable → `src/`
   - Visualisations → `outputs/`

3. **Suivre les conventions**:
   - Nomenclature des branches
   - Messages de commit avec SAE-XX
   - Format des notebooks

4. **Proposer du code robuste**:
   - Gestion des erreurs
   - Progress bars avec tqdm
   - Commentaires clairs

5. **Être pédagogique**:
   - Expliquer les choix techniques
   - Suggérer des ressources
   - Pointer vers la documentation

6. **Maintenir la cohérence**:
   - Synchroniser `docs/PROJECT-PLAN.md` avec Linear
   - Cocher les tâches au fur et à mesure
   - Vérifier que chaque story appartient bien à une Epic
   - Mettre à jour le plan quand une story est complétée

---

## 📊 Gestion des Stories et Epics

### Structure dans Linear

**Epic (Initiative/Project):**
- Regroupement logique de stories
- Correspond à une phase majeure du projet
- Exemple: "Epic 1 - Setup & Data Loading"

**Story (Issue):**
- Unité de travail assignable
- Contient une checklist de tâches
- Liée à une Epic parent
- Format: SAE-XX

**Exemple de story complète:**
```markdown
# SAE-64: Chargement Business JSON

## Epic
Epic 1 - Setup & Data Loading

## Description
Charger et explorer le fichier yelp_academic_dataset_business.json

## Tasks
- [ ] Créer notebook 01_business_loading.ipynb
- [ ] Charger le JSON avec pandas
- [ ] Explorer les colonnes (.info(), .describe())
- [ ] Documenter les insights

## Critères d'acceptation
- Notebook fonctionnel et documenté
- Statistiques de base extraites
- Pas d'erreurs de chargement
```

### Workflow complet avec Epics

1. **Identifier l'Epic** de la story
2. **Lire la checklist** dans la description
3. **Travailler tâche par tâche** en les cochant
4. **Créer la PR** quand toutes les tâches sont complètes
5. **Mettre à jour PROJECT-PLAN.md** après merge

---

**Questions ?** Contacter l'équipe sur Discord ou Linear.
