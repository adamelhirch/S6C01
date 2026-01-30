# 🚀 Guide de Démarrage Rapide - S6C01

**Bienvenue dans le projet d'analyse Yelp!**

## 🎯 Étape 1: Cloner le projet (5 min)

```bash
# Cloner le repo
git clone https://github.com/adamelhirch/S6C01.git
cd S6C01

# Vérifier que vous êtes sur main
git branch
# Devrait afficher: * main
```

## 🐍 Étape 2: Setup Python (10 min)

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer le venv
# Sur macOS/Linux:
source venv/bin/activate

# Sur Windows:
venv\Scripts\activate

# Mettre à jour pip
pip install --upgrade pip

# Installer toutes les dépendances
pip install -r requirements.txt
```

### Vérification de l'installation

```bash
python -c "import pandas; import nltk; import sklearn; print('✅ Tout fonctionne!')"
```

## 📚 Étape 3: Télécharger les ressources NLTK (2 min)

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab')"
```

## 📂 Étape 4: Ajouter les données (5 min)

1. Téléchargez les 3 fichiers JSON depuis le sujet
2. Placez-les dans `data/raw/`:
   - `yelp_academic_dataset_business.json`
   - `yelp_academic_reviews4students.jsonl`
   - `yelp_academic_dataset_user4students.jsonl`

**⚠️ Important:** Les fichiers JSON ne sont PAS versionnés sur Git (trop gros). Chacun doit les avoir localement.

## 🌿 Étape 5: Créer VOTRE branche (2 min)

```bash
# Remplacez "votre-prenom" par votre vrai prénom
# Remplacez "sae-XX" par le numéro de la story que vous prenez

git checkout -b votre-prenom/sae-XX-description

# Exemple:
# git checkout -b natalia/sae-64-chargement-business
# git checkout -b ewen/sae-65-chargement-reviews
# git checkout -b manolo/sae-66-chargement-users
```

### Vérifier votre branche

```bash
git branch
# Devrait afficher: * votre-prenom/sae-XX-description
```

## 💻 Étape 6: Lancer Jupyter (1 min)

```bash
# S'assurer que le venv est activé
# Puis lancer Jupyter
jupyter notebook

# Ou Jupyter Lab si vous préférez:
jupyter lab
```

Un onglet devrait s'ouvrir dans votre navigateur!

## 📝 Étape 7: Prendre une story dans Linear

1. Allez sur https://linear.app/sae6c01
2. Regardez le Backlog
3. Choisissez une story marquée "Todo"
4. Assignez-la vous et passez-la en "In Progress"
5. Notez le numéro (ex: SAE-64)

## 🎨 Étape 8: Travailler sur votre story

### Créer un notebook

```bash
# Dans notebooks/
# Nommez-le selon votre story
notebooks/01_chargement_business.ipynb
notebooks/02_chargement_reviews.ipynb
```

### Ou créer un script Python

```bash
# Dans src/
src/my_analysis.py
```

## ✅ Étape 9: Commiter votre travail

```bash
# Voir vos modifications
git status

# Ajouter vos fichiers
git add notebooks/mon_notebook.ipynb
# OU
git add src/mon_script.py

# Commiter avec le numéro de story
git commit -m "SAE-XX Description de ce que vous avez fait

Co-Authored-By: Claude (gemini-claude-sonnet-4-5-thinking) <noreply@anthropic.com>"

# Exemple:
# git commit -m "SAE-64 Chargement et exploration données business
#
# - Chargement du fichier JSON
# - Vérification des colonnes
# - Statistiques de base
#
# Co-Authored-By: Claude (gemini-claude-sonnet-4-5-thinking) <noreply@anthropic.com>"
```

## 🚀 Étape 10: Pousser votre branche

```bash
# Pousser votre branche sur GitHub
git push origin votre-prenom/sae-XX-description

# Exemple:
# git push origin natalia/sae-64-chargement-business
```

## 🔀 Étape 11: Créer une Pull Request

1. Allez sur https://github.com/adamelhirch/S6C01
2. Vous verrez un bouton "Compare & pull request" → Cliquez
3. Titre: `SAE-XX Description`
4. Description: Résumé de ce que vous avez fait
5. Créez la PR
6. Demandez une review à un coéquipier

## 🎉 Étape 12: Après le merge

```bash
# Revenir sur main
git checkout main

# Récupérer les derniers changements
git pull origin main

# Supprimer votre branche locale (elle est déjà merged)
git branch -d votre-prenom/sae-XX-description
```

---

## 🆘 Problèmes courants

### "command not found: python3"
**Solution:** Utilisez `python` au lieu de `python3`

### "Permission denied" lors du push
**Solution:** Vérifiez que vous êtes bien collaborateur du repo GitHub

### "Import Error: No module named 'pandas'"
**Solution:** Vérifiez que votre venv est activé (`source venv/bin/activate`)

### Fichiers JSON trop gros pour Git
**Solution:** C'est normal! Ils ne doivent PAS être versionnés. Le `.gitignore` les exclut.

### Conflit de merge
**Solution:**
```bash
git checkout main
git pull origin main
git checkout votre-branche
git merge main
# Résoudre les conflits dans les fichiers
git add .
git commit -m "Résolution conflits"
```

---

## 📚 Ressources utiles

- **Linear (Stories):** https://linear.app/sae6c01
- **GitHub (Code):** https://github.com/adamelhirch/S6C01
- **Workflow détaillé:** Voir `docs/WORKFLOW.md`
- **Plan du projet:** Voir `docs/PROJECT-PLAN.md`

---

## 🤝 Répartition suggérée (Semaine 1)

**Personne 1 (Adam?):**
- SAE-62: Configuration Linear ↔ GitHub
- SAE-96: Nettoyage Business

**Personne 2 (Natalia?):**
- SAE-64: Chargement Business
- SAE-67: Dashboard Profils Reviewers

**Personne 3 (Ewen?):**
- SAE-65: Chargement Reviews
- SAE-97: Nettoyage Reviews

**Personne 4 (Manolo?):**
- SAE-66: Chargement Users
- SAE-98: Nettoyage Users

---

**Questions?** Demandez sur Discord ou Linear! 🚀
