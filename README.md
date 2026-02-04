# 📊 S6C01 - Analyse de Données Yelp

**Projet SAE S6C01 - Analyse de Grandes Données**
**BUT Informatique - Semestre 6 (2025-2026)**

---

## 🤖 AI Context (Antigravity, Claude & assistants IA)

> **Type de projet**: Data Science / Machine Learning / NLP (Analyse de données Yelp)  
> **Environnement**: Python 3.12+ avec Jupyter Notebooks  
> **Méthodologie**: Agile (Linear) + Git/GitHub

### 🛠️ Technologies principales
- **Data**: `pandas`, `numpy` (manipulation), `parquet` (stockage optimisé)
- **Viz**: `matplotlib`, `seaborn`, `plotly`
- **NLP**: `nltk`, `scikit-learn`, `transformers`
- **ML**: `scikit-learn`, `torch` (PyTorch)
- **Notebooks**: `jupyter`

### 📊 Architecture des données
```
data/raw/*.json → notebooks/XX_*.ipynb → data/cleaned/*.parquet → outputs/
```

### 🔧 Workflows et Documentation

**Pour les IA (Antigravity, claude-cli):**
- `.claude/PROJECT_CONTEXT.md` - **Chargé automatiquement** - Contexte complet du projet
- `.agent/workflows/` - Workflows Antigravity (`/setup-environment`, `/start-development`, etc.)
- `docs/AI_INSTRUCTIONS.md` - Conventions de code et patterns

**Pour les humains (guides détaillés):**
- `docs/QUICKSTART.md` - 🚀 Guide démarrage rapide
- `docs/WORKFLOW_SETUP.md` - Configuration environnement
- `docs/WORKFLOW_DEVELOPMENT.md` - Workflow Git complet
- `docs/WORKFLOW_JUPYTER.md` - Travailler avec Jupyter
- `docs/WORKFLOW_LINEAR_INTEGRATION.md` - Intégration Linear ↔ GitHub
- `docs/PROJECT-PLAN.md` - Plan du projet (Epics/Stories)

**Voir [`docs/README.md`](docs/README.md) pour l'index complet.**

### 🤖 Intégration Linear ↔ GitHub (Automatique)

Les assistants IA avec MCP Linear et GitHub automatisent:
- ✅ Ajout des liens de branche dans Linear
- ✅ Création de PR quand story terminée
- ✅ Ajout du lien PR dans Linear
- ✅ Passage en "In Review" automatique

Voir `.claude/PROJECT_CONTEXT.md` pour les détails.

### ⚠️ Points CRITIQUES
- 🚨 **Fichiers JSON dans `data/raw/` NON versionnés** (trop volumineux ~6 GB)
- 🔄 **Toujours travailler dans une branche** (format: `prenom/sae-XX-description`)
- 📝 **Commits avec Linear** (format: `SAE-XX Description`)
- 🐍 **Toujours activer le venv** (`source venv/bin/activate`)

---

## 👥 Équipe

- **Adam EL HIRCH** - [@adamelhirch](https://github.com/adamelhirch)
- **Natalia ROS** - [@rsnataliaa](https://github.com/rsnataliaa)
- **Ewen MONTOUT** - [@ewen-montout](https://github.com/ewen-montout)
- **Manolo BRACH** - [@reyyko](https://github.com/reyyko)
- **Lotfi MELOUANE** - [@lotfimln](https://github.com/lotfimln)
- 
## 📖 Description

Projet d'analyse de données Yelp utilisant Python, Machine Learning et NLP. L'objectif est d'explorer le dataset Yelp Academic pour extraire des insights sur les commerces, les avis clients et les comportements utilisateurs.

## 🎯 Objectifs

- **Epic 1**: Setup environnement + Chargement et nettoyage des données JSON
- **Epic 2**: Preprocessing & Text Cleaning (NLP)
- **Epic 3**: Text Representation (TF-IDF, Word2Vec, Embeddings)
- **Epic 4**: ML Classique (Classification, Clustering, Recommandation)
- **Epic 5**: LLM Local (BERT, HuggingFace)
- **Epic 6**: Documentation & Rendu Final

## 📁 Structure du Projet

```
S6C01-Yelp-Analysis/
├── README.md                   # Ce fichier
├── requirements.txt            # Dépendances Python
├── .gitignore                 # Fichiers ignorés par Git
│
├── data/                      # Données (NON versionnées)
│   ├── raw/                   # JSON bruts Yelp
│   │   ├── yelp_academic_dataset_business.json
│   │   ├── yelp_academic_reviews4students.json
│   │   └── yelp_academic_dataset_user4students.json
│   └── cleaned/               # Données nettoyées (parquet)
│       ├── business_clean.parquet
│       ├── reviews_clean.parquet
│       └── users_clean.parquet
│
├── notebooks/                 # Jupyter notebooks
│   ├── 01_data_loading.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_eda_dashboards.ipynb
│   └── ...
│
├── src/                       # Code source Python

│
├── outputs/                   # Visualisations et rapports
│   ├── figures/
│   └── reports/
│
└── docs/                      # Documentation
    └── stories/               # Documentation par story
        ├── epic1/
        ├── epic2/
        └── ...
```

## 🚀 Installation

### 🆕 Nouveau collaborateur?

**👉 Suivez le guide de démarrage rapide: [docs/QUICKSTART.md](docs/QUICKSTART.md)**

Ce guide vous accompagne pas à pas pour configurer votre environnement et créer votre première branche en 30 minutes!

---

### Installation manuelle

### 1. Cloner le repository

```bash
git clone https://github.com/adamelhirch/S6C01-Yelp-Analysis.git
cd S6C01-Yelp-Analysis
```

### 2. Créer l'environnement virtuel Python

```bash
# Créer le venv
python3 -m venv venv

# Activer le venv
# Sur macOS/Linux:
source venv/bin/activate
# Sur Windows:
venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Télécharger les ressources NLTK

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### 5. Ajouter les données Yelp

Téléchargez les fichiers JSON depuis le sujet et placez-les dans `data/raw/`:
- `yelp_academic_dataset_business.json`
- `yelp_academic_reviews4students.jsonl`
- `yelp_academic_dataset_user4students.jsonl`

**⚠️ Important**: Les fichiers JSON ne sont PAS versionnés sur Git (trop volumineux).

## 📝 Utilisation

### Lancer Jupyter

```bash
jupyter notebook
```

Ouvrez ensuite les notebooks dans `notebooks/` dans l'ordre numérique.

### Workflow de développement

Le projet suit une méthodologie Agile avec tracking sur [Linear](https://linear.app/sae6c01).

## 🔄 Workflow Git + Linear

### Prendre une story

1. Allez sur [Linear](https://linear.app/sae6c01)
2. Prenez une story (Backlog → In Progress)
3. Notez le numéro (ex: SAE-64)

### Créer une branche

```bash
# Depuis Linear (bouton "Create branch") OU manuellement:
git checkout -b votre-prenom/sae-XX-description
```

### Travailler et commiter

```bash
# Faire vos modifications
git add .
git commit -m "SAE-XX Description de votre travail"
```

### Pousser et créer une PR

```bash
git push origin votre-prenom/sae-XX-description
```

Ensuite sur GitHub:
1. Créer une Pull Request
2. Titre: "SAE-XX Description"
3. La PR sera automatiquement liée dans Linear

### Après review

```bash
# Merger la PR sur GitHub
# La story passera automatiquement à Done dans Linear
```

## 📊 Datasets

- **Business**: ~150k commerces (restaurants, bars, hôtels)
- **Reviews**: ~6M avis textuels
- **Users**: ~2M profils utilisateurs

## 🛠️ Technologies

- **Python 3.12+**
- **Pandas** - Manipulation de données
- **Matplotlib/Seaborn** - Visualisations
- **NLTK/Scikit-learn** - NLP et ML
- **HuggingFace Transformers** - LLMs
- **Jupyter** - Notebooks interactifs

## 📈 Progression

Suivez l'avancement du projet sur [Linear](https://linear.app/sae6c01).

## 📄 Licence

Projet académique - BUT Informatique S6 (2025-2026)

## 🤝 Contribution

1. Prenez une story dans Linear
2. Créez une branche
3. Faites vos modifications
4. Créez une Pull Request
5. Demandez une review

---

**Questions?** Contactez l'équipe sur Discord ou Linear.
