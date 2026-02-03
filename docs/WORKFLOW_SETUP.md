# Guide Setup - Configuration Environnement S6C01

**Pour utilisateurs claude-cli et développement manuel**

## Vue d'ensemble

Ce guide vous aide à configurer votre environnement de développement pour le projet S6C01 (Analyse Yelp).

## Prérequis

- Python 3.12+ installé
- Git configuré
- Accès au repository GitHub
- Données Yelp téléchargées

## Étapes de configuration

### 1. Cloner le repository (si pas déjà fait)

```bash
git clone https://github.com/adamelhirch/S6C01.git
cd S6C01
```

### 2. Vérifier Python

```bash
python3 --version
# Résultat attendu: Python 3.12.x ou supérieur
```

Sur Windows, utilisez `python` au lieu de `python3`.

### 3. Créer l'environnement virtuel

```bash
python3 -m venv venv
```

### 4. Activer l'environnement virtuel

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

Vérification: Votre prompt devrait afficher `(venv)` au début.

### 5. Mettre à jour pip

```bash
pip install --upgrade pip
```

### 6. Installer les dépendances

```bash
pip install -r requirements.txt
```

**Note:** Cette étape peut prendre 5-10 minutes (installation de PyTorch, Transformers, etc.)

### 7. Télécharger les ressources NLTK

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab')"
```

### 8. Vérifier la structure des données

```bash
ls -lh data/raw/
```

**Fichiers attendus:**
- `yelp_academic_dataset_business.json` (~120 MB)
- `yelp_academic_reviews4students.jsonl` (~5 GB)
- `yelp_academic_dataset_user4students.jsonl` (~600 MB)

**Si les fichiers manquent:**
1. Téléchargez-les depuis le sujet SAE
2. Placez-les dans le dossier `data/raw/`

### 9. Test final

```bash
python -c "import pandas as pd; import numpy as np; import nltk; import transformers; print('✅ Installation réussie!')"
```

## Checklist finale

- [ ] Environnement virtuel créé et activé
- [ ] Toutes les dépendances installées (requirements.txt)
- [ ] Ressources NLTK téléchargées
- [ ] Données Yelp présentes dans `data/raw/`
- [ ] Test d'import réussi

## Problèmes courants

### "command not found: python3"
**Solution:** Utilisez `python` au lieu de `python3`

### "Permission denied" lors de l'activation du venv
**Solution Windows:** Exécutez PowerShell en administrateur et tapez:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Imports échouent même après installation
**Solution:** Vérifiez que le venv est activé (vous devez voir `(venv)` dans votre prompt)

### Données manquantes
**Solution:** Les fichiers JSON ne sont PAS versionnés sur Git. Chaque membre doit les télécharger individuellement depuis le sujet SAE.

## Prochaines étapes

Une fois l'environnement configuré, consultez:
- `WORKFLOW_DEVELOPMENT.md` - Pour commencer à travailler sur une story
- `WORKFLOW_JUPYTER.md` - Pour lancer Jupyter et créer des notebooks
- `WORKFLOW_LINEAR_INTEGRATION.md` - Pour comprendre l'intégration Linear ↔ GitHub

## Commandes rapides de référence

**Activer venv (macOS/Linux):**
```bash
source venv/bin/activate
```

**Activer venv (Windows):**
```cmd
venv\Scripts\activate
```

**Désactiver venv:**
```bash
deactivate
```

**Vérifier installation:**
```bash
pip list
```
