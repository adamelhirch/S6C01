# Guide de Collaboration - S6C01

## 🎯 Avant de commencer

Assurez-vous d'avoir:
- ✅ Accès au workspace Linear: https://linear.app/sae6c01
- ✅ MCP Linear installé localement (pour Claude)
- ✅ Accès au repo GitHub: https://github.com/adamelhirch/S6C01

## 🚀 Setup Initial

### 1. Cloner le projet

```bash
git clone https://github.com/adamelhirch/S6C01.git
cd S6C01
```

### 2. Créer l'environnement Python

```bash
# Créer le venv
python3 -m venv venv

# Activer
source venv/bin/activate  # macOS/Linux
# OU
venv\Scripts\activate     # Windows

# Installer dépendances
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Télécharger les ressources NLTK

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### 4. Ajouter les données

Placez les fichiers JSON Yelp dans `data/raw/`:
- `yelp_academic_dataset_business.json`
- `yelp_academic_reviews4students.jsonl`
- `yelp_academic_dataset_user4students.jsonl`

## 🔄 Workflow Quotidien

### 1. Prendre une story dans Linear

**Via Claude (recommandé):**
- Demandez à Claude: "Quelles sont les prochaines stories à faire?"
- Claude consultera automatiquement Linear via MCP
- Il vous montrera les stories disponibles

**Via l'interface Linear:**
- https://linear.app/sae6c01
- Choisir une story dans le Backlog
- L'assigner à vous et passer en "In Progress"

### 2. Créer une branche

```bash
git checkout main
git pull origin main
git checkout -b prenom/sae-XX-description
```

**Exemple:** `adam/sae-64-chargement-business`

### 3. Travailler

```bash
# Faire vos modifications
# Tester votre code

# Vérifier les changements
git status
git diff
```

### 4. Commiter

```bash
git add fichiers-modifies
git commit -m "SAE-XX Description du changement

Co-Authored-By: Claude (gemini-claude-sonnet-4-5-thinking) <noreply@anthropic.com>"
```

**Format du message:**
- Toujours inclure le numéro de story (SAE-XX)
- Message descriptif et concis
- Co-Authored-By si vous utilisez Claude

### 5. Pousser et créer une PR

```bash
git push origin prenom/sae-XX-description
```

Sur GitHub:
1. Créer une Pull Request
2. Titre: `SAE-XX Description`
3. Demander une review

### 6. Après le merge

```bash
git checkout main
git pull origin main
git branch -d prenom/sae-XX-description
```

## 💡 Utiliser Claude avec Linear MCP

### Commandes utiles pour Claude

**Voir l'état du projet:**
```
"Où en est le projet?"
"Quelles sont les prochaines stories?"
"Montre-moi les stories en cours"
```

**Travailler sur une story:**
```
"Aide-moi sur SAE-64"
"Je veux travailler sur le chargement des données business"
```

**Claude va automatiquement:**
- ✅ Consulter Linear pour voir la story
- ✅ Lire les critères d'acceptation
- ✅ Vous guider dans l'implémentation
- ✅ Ajouter des commentaires sur la story
- ✅ Mettre à jour le statut quand c'est terminé

## 🎨 Conventions

### Branches
- Format: `prenom/sae-XX-description-courte`
- Toujours partir de `main` à jour
- Une branche = une story

### Commits
- Inclure SAE-XX dans le message
- Message clair et descriptif
- Commits atomiques (un changement logique)

### Code
- Tester avant de pusher
- Commenter les parties complexes
- Suivre les fonctions existantes dans `src/`

### Pull Requests
- Titre avec SAE-XX
- Description des changements
- Review obligatoire avant merge

## 📂 Structure du Projet

```
S6C01/
├── README.md              # Documentation principale
├── requirements.txt       # Dépendances Python
├── .gitignore            # Fichiers ignorés
│
├── data/                 # Données (NON versionnées)
│   ├── raw/              # JSON bruts
│   └── cleaned/          # Parquet nettoyés
│
├── notebooks/            # Jupyter notebooks
│   ├── 01_*.ipynb
│   └── ...
│
├── src/                  # Code source réutilisable
│   ├── data_loading.py   # Chargement JSON
│   ├── data_cleaning.py  # Nettoyage données
│   └── preprocessing.py  # Preprocessing NLP
│
├── outputs/              # Visualisations et rapports
│   ├── figures/
│   └── reports/
│
└── docs/                 # Documentation
    └── WORKFLOW.md       # Ce fichier
```

## 🚨 Problèmes Courants

### Conflit de merge
```bash
git checkout main
git pull origin main
git checkout votre-branche
git merge main
# Résoudre les conflits dans les fichiers
git add .
git commit -m "Résolution conflits"
```

### Erreur import pandas/nltk
```bash
# Vérifier que le venv est activé
which python  # doit pointer vers votre venv

# Réinstaller les dépendances
pip install -r requirements.txt
```

### Fichiers data trop gros pour Git
**Normal!** Les fichiers dans `data/` ne doivent PAS être versionnés.
Le `.gitignore` les exclut automatiquement.

## 📊 Suivi du Projet

- **Linear:** Tracking des stories et epics
  - https://linear.app/sae6c01
- **GitHub:** Code et Pull Requests
  - https://github.com/adamelhirch/S6C01

## 🤝 Bonnes Pratiques

1. **Pull régulièrement** pour rester à jour
2. **Commiter souvent** avec des messages clairs
3. **Demander des reviews** pour apprendre ensemble
4. **Utiliser Claude** pour vous aider (il a accès à Linear!)
5. **Documenter** les décisions importantes
6. **Tester** avant de pusher

## 💬 Communication

- **Linear:** Pour les questions sur les stories
- **GitHub:** Pour les reviews de code
- **Discord/Messages:** Pour la coordination d'équipe

---

**Questions?** Demandez à Claude ou à l'équipe! 🚀
