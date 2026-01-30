# Guide de Collaboration - S6C01

## 🔄 Workflow Git + Linear

### 1. Prendre une story dans Linear

1. Allez sur https://linear.app/sae6c01
2. Choisissez une story dans le Backlog
3. Assignez-la vous et passez-la à "In Progress"
4. Notez le numéro (ex: SAE-64)

### 2. Créer une branche

```bash
git checkout main
git pull origin main
git checkout -b votre-prenom/sae-XX-description-courte
```

Exemple: `adam/sae-64-chargement-business`

### 3. Travailler sur la story

```bash
# Faire vos modifications
# ...

# Vérifier les changements
git status
git diff

# Ajouter les fichiers modifiés
git add fichiers-modifiés

# Commiter avec le numéro de story
git commit -m "SAE-XX Description du changement"
```

**Format du message de commit:**
```
SAE-XX Titre court

Description plus détaillée si nécessaire.

Co-Authored-By: Claude (gemini-claude-sonnet-4-5-thinking) <noreply@anthropic.com>
```

### 4. Pousser et créer une Pull Request

```bash
git push origin votre-prenom/sae-XX-description
```

Sur GitHub:
1. Allez sur https://github.com/adamelhirch/S6C01
2. Cliquez "New Pull Request"
3. Titre: `SAE-XX Description`
4. Description: Résumé des changements
5. Créez la PR

### 5. Review et Merge

1. Demandez une review à un coéquipier
2. Discutez des changements si nécessaire
3. Une fois approuvé: Merge la PR
4. La story passera automatiquement à "Done" dans Linear

### 6. Nettoyage

```bash
git checkout main
git pull origin main
git branch -d votre-prenom/sae-XX-description
```

## 📝 Conventions

### Branches
- Format: `prenom/sae-XX-description`
- Toujours partir de `main` à jour
- Une branche = une story

### Commits
- Message clair et descriptif
- Inclure le numéro SAE-XX
- Commits atomiques (un changement logique par commit)

### Pull Requests
- Titre avec SAE-XX
- Description complète
- Review obligatoire avant merge

## 🚨 Problèmes courants

### Conflit de merge
```bash
git checkout main
git pull origin main
git checkout votre-branche
git merge main
# Résoudre les conflits
git add .
git commit -m "Résolution conflits"
```

### Oubli de pull avant de créer une branche
```bash
git checkout main
git pull origin main
git checkout votre-branche
git rebase main
```

## 💡 Bonnes pratiques

1. **Pull régulièrement** pour rester à jour
2. **Commiter souvent** avec des messages clairs
3. **Tester avant de pusher**
4. **Demander des reviews** pour apprendre
5. **Documenter** les décisions importantes

## 📞 Besoin d'aide?

- Discord de l'équipe
- Linear pour les questions sur les stories
- GitHub Discussions pour les questions techniques
