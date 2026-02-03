# Guide Développement - Workflow complet Git + Linear

**Pour utilisateurs claude-cli et développement manuel**

## Vue d'ensemble

Ce guide décrit le workflow complet pour prendre une story Linear, développer, créer une PR et merger.

## Workflow en 11 étapes

### 1️⃣ Récupérer une story sur Linear

1. Aller sur [Linear - SAE6C01](https://linear.app/sae6c01)
2. Naviguer dans le Backlog
3. Choisir une story marquée "Todo" ou "Backlog"
4. Cliquer dessus et cliquer "Start" (ou glisser vers "In Progress")
5. S'assigner la story
6. Noter le numéro (ex: `SAE-64`)

### 2️⃣ Mettre à jour votre branche main locale

```bash
git checkout main
git pull origin main
```

### 3️⃣ Créer une branche Git

**Nomenclature:**
```
prenom/sae-XX-description-courte
```

**Exemples:**
- `adam/sae-64-data-cleaning`
- `natalia/sae-72-tfidf-implementation`
- `ewen/sae-80-bert-model`
- `manolo/sae-95-dashboard-semantic`

**Créer la branche:**
```bash
git checkout -b prenom/sae-XX-description-courte
```

**Exemple concret:**
```bash
git checkout -b adam/sae-68-shared-library
```

### 4️⃣ Activer l'environnement virtuel

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

### 5️⃣ Développer votre solution

**Option A: Créer/modifier un notebook**
```bash
jupyter notebook
# Créer notebooks/XX_description.ipynb
```

**Option B: Créer/modifier du code Python**
```bash
# Éditer src/mon_module.py
```

**Option C: Les deux**
- Notebook pour exploration
- Code dans `src/` pour fonctions réutilisables

### 6️⃣ Tester votre code

**Pour notebooks:**
1. `Kernel → Restart & Run All`
2. Vérifier qu'il n'y a pas d'erreurs
3. `Cell → All Output → Clear` avant de commiter

**Pour scripts Python:**
```bash
python src/mon_script.py
```

### 7️⃣ Voir vos modifications

```bash
git status
```

Vous verrez les fichiers modifiés/créés en rouge.

### 8️⃣ Ajouter vos fichiers

```bash
# Ajouter des fichiers spécifiques (recommandé)
git add notebooks/XX_description.ipynb
git add src/mon_module.py

# OU ajouter tous les fichiers modifiés
git add .
```

### 9️⃣ Commiter vos changements

**Format du message:**
```
SAE-XX Titre court (50 caractères max)

- Détail 1
- Détail 2
- Détail 3

Co-Authored-By: Claude (gemini-claude-sonnet-4-5-thinking) <noreply@anthropic.com>
```

**Exemple:**
```bash
git commit -m "SAE-68 Add shared library for code reuse

- Created src/shared/data_loader.py
- Added Parquet loading utilities
- Updated notebook to use shared functions

Co-Authored-By: Claude (gemini-claude-sonnet-4-5-thinking) <noreply@anthropic.com>"
```

**Pourquoi `Co-Authored-By`?**
Si vous avez utilisé Claude CLI pour vous aider, c'est une bonne pratique de le mentionner.

### 🔟 Pousser votre branche

**Premier push:**
```bash
git push -u origin prenom/sae-XX-description-courte
```

**Pushs suivants:**
```bash
git push
```

### 1️⃣1️⃣ Créer une Pull Request

**Option A: Via GitHub Web**

1. Aller sur https://github.com/adamelhirch/S6C01
2. Vous verrez une bannière "Compare & pull request" → Cliquer
3. Remplir:
   - **Titre:** `SAE-XX Description courte`
   - **Description:** Résumé de vos changements
4. **Base:** `main` (vérifier)
5. **Compare:** `prenom/sae-XX-description`
6. Assigner des reviewers (coéquipiers)
7. Cliquer "Create pull request"

**Option B: Via GitHub CLI (si installé)**

```bash
gh pr create --title "SAE-XX Description" --body "Description de la PR" --base main
```

## Après la création de la PR

### Lien automatique Linear ↔ GitHub

Si le workflow d'intégration est configuré, **automatiquement**:
1. Le lien de la PR sera ajouté à la story Linear
2. La story passera en état "In Review"

Sinon, vous pouvez ajouter le lien manuellement dans Linear (Resources).

### Attendre la review

- Les coéquipiers vont lire votre code
- Ils peuvent laisser des commentaires
- Vous devez répondre et faire les modifications demandées si nécessaire

### Faire des modifications suite aux commentaires

```bash
# Modifier les fichiers
# ...

# Commiter les changements
git add .
git commit -m "SAE-XX Address review comments

- Fix issue X
- Improve Y"

# Pousser (la PR se met à jour automatiquement)
git push
```

### Merger la PR

**Une fois approuvée:**

**Option A: Merge via GitHub Web**
1. Cliquer "Merge pull request" sur GitHub
2. Confirmer le merge
3. Supprimer la branche sur GitHub (optionnel mais recommandé)

**Option B: Merge via CLI**
```bash
gh pr merge --merge
```

**Après le merge:**
La story passe automatiquement à "Done" dans Linear ✅

## Nettoyage après merge

```bash
# Revenir sur main
git checkout main

# Récupérer les derniers changements (incluant votre merge)
git pull origin main

# Supprimer votre branche locale (elle est déjà mergée)
git branch -d prenom/sae-XX-description
```

## Checklist complète

**Avant de commencer:**
- [ ] Story prise et assignée sur Linear
- [ ] Story passée en "In Progress"
- [ ] Numéro de story noté (SAE-XX)

**Développement:**
- [ ] Branche créée avec bonne nomenclature
- [ ] Environnement virtuel activé
- [ ] Code écrit et testé
- [ ] Outputs de notebooks nettoyés si applicable

**Commit & Push:**
- [ ] Fichiers ajoutés avec `git add`
- [ ] Message de commit formaté correctement
- [ ] Branche poussée sur GitHub

**Pull Request:**
- [ ] PR créée avec titre formaté (SAE-XX)
- [ ] Description claire de ce qui a été fait
- [ ] Reviewers assignés
- [ ] Lien PR ajouté dans Linear (automatique ou manuel)
- [ ] Story en "In Review" dans Linear

**Après merge:**
- [ ] Story "Done" dans Linear
- [ ] Branche locale supprimée
- [ ] Retour sur main et pull

## Cas particuliers

### Plusieurs commits sur la même branche

C'est OK! Vous pouvez faire plusieurs commits:

```bash
# Premier commit
git add file1.py
git commit -m "SAE-XX Initial implementation"
git push

# Deuxième commit
git add file2.py
git commit -m "SAE-XX Add tests"
git push

# Etc.
```

La PR contiendra tous les commits.

### Conflit de merge

Si votre branche a des conflits avec `main`:

```bash
# Mettre à jour main
git checkout main
git pull origin main

# Revenir sur votre branche
git checkout prenom/sae-XX-description

# Merger main dans votre branche
git merge main

# Résoudre les conflits dans les fichiers
# (Git vous indiquera quels fichiers ont des conflits)

# Après résolution
git add .
git commit -m "SAE-XX Resolve merge conflicts"
git push
```

### Modifier une PR existante

Il suffit de pousser de nouveaux commits sur la même branche:

```bash
# Modifier les fichiers
# ...

git add .
git commit -m "SAE-XX Update based on feedback"
git push
```

La PR se mettra à jour automatiquement.

## Conseils et bonnes pratiques

### Commits fréquents

Commitez souvent (toutes les 30 min - 1h de travail). C'est plus facile de revenir en arrière si nécessaire.

### Messages de commit descriptifs

Évitez:
- ❌ "Fix"
- ❌ "Update"
- ❌ "WIP"

Préférez:
- ✅ "SAE-XX Add TF-IDF vectorization function"
- ✅ "SAE-XX Fix data loading bug for large files"
- ✅ "SAE-XX Improve visualization rendering speed"

### Tester avant de pousser

Toujours tester que votre code fonctionne avant de `git push`.

### PRs de taille raisonnable

Essayez de garder vos PRs à une taille gérable (< 500 lignes de code). C'est plus facile à reviewer.

## Problèmes courants

### "Your branch is behind 'origin/main'"

**Solution:**
```bash
git checkout main
git pull origin main
git checkout votre-branche
git merge main
```

### "Permission denied" lors du push

**Solution:** Vérifiez que vous êtes collaborateur du repo GitHub.

### "Merge conflict"

**Solution:** Voir section "Conflit de merge" ci-dessus.

### PR ne se crée pas automatiquement dans Linear

**Solution:** Ajoutez le lien manuellement dans Linear (Resources → Add link → PR URL).

## Ressources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Linear Documentation](https://linear.app/docs)

## Prochaines étapes

- `WORKFLOW_LINEAR_INTEGRATION.md` - Comprendre l'intégration Linear ↔ GitHub
- `WORKFLOW_JUPYTER.md` - Travailler avec Jupyter
- `AI_INSTRUCTIONS.md` - Conventions de code et bonnes pratiques
