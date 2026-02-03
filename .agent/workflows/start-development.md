---
description: Commencer une nouvelle tâche de développement
---

# Workflow Développement S6C01

Ce workflow guide le processus complet pour prendre une story Linear et créer une Pull Request.

## Étapes

### 1. Récupérer une story sur Linear

1. Aller sur [Linear - SAE6C01](https://linear.app/sae6c01)
2. Sélectionner une story dans le Backlog
3. Déplacer vers "In Progress"
4. Noter le numéro (ex: `SAE-64`)

### 2. Créer une branche Git

**Option A: Depuis Linear (recommandé)**

Cliquer sur le bouton "Create branch" dans Linear, qui générera automatiquement:
```
prenom/sae-XX-description-courte
```

**Option B: Manuellement**

```bash
git checkout main
git pull origin main
git checkout -b prenom/sae-XX-description-courte
```

Remplacer:
- `prenom` par votre prénom (ex: adam, natalia, ewen, manolo, lotfi)
- `XX` par le numéro de story
- `description-courte` par une courte description en kebab-case

Exemples:
- `adam/sae-64-data-cleaning`
- `natalia/sae-72-tfidf-implementation`
- `ewen/sae-80-bert-model`

### 3. Activer l'environnement virtuel

// turbo
```bash
source venv/bin/activate
```

### 4. Faire vos modifications

Travaillez sur votre story:
- Créer/modifier des notebooks dans `notebooks/`
- Créer/modifier du code dans `src/`
- Ajouter des visualisations dans `outputs/`

### 5. Tester votre code

Vérifier que tout fonctionne:
- Relancer les cellules de votre notebook
- Vérifier qu'il n'y a pas d'erreurs
- Vérifier que les outputs sont corrects

### 6. Commiter vos changements

```bash
git add .
git commit -m "SAE-XX Description de votre travail

- Détail 1
- Détail 2
- Détail 3"
```

⚠️ **Important**: Le message de commit doit:
- Commencer par `SAE-XX` (numéro de la story)
- Avoir une description courte sur la première ligne
- Avoir une ligne vide
- Avoir des détails sous forme de liste avec `-`

### 7. Pousser la branche

```bash
git push origin prenom/sae-XX-description-courte
```

Si c'est votre premier push:
```bash
git push -u origin prenom/sae-XX-description-courte
```

### 8. Créer une Pull Request

1. Aller sur [GitHub - S6C01](https://github.com/adamelhirch/S6C01)
2. Cliquer sur "Compare & pull request"
3. Remplir:
   - **Titre**: `SAE-XX Description courte`
   - **Description**: Résumé de vos changements
4. Assigner des reviewers (membres de l'équipe)
5. Créer la PR

### 9. Attendre la review

- La PR sera automatiquement liée dans Linear
- Attendez les commentaires/approbations
- Faites les modifications demandées si nécessaire

### 10. Merger la PR

Une fois approuvée:
1. Merger la PR sur GitHub
2. La story passera automatiquement à "Done" dans Linear ✅

## Résultat attendu

- ✅ Story prise sur Linear et marquée "In Progress"
- ✅ Branche créée avec nomenclature correcte
- ✅ Code écrit et testé
- ✅ Commit(s) avec message formaté
- ✅ PR créée et liée à Linear
- ✅ Après merge: Story "Done" ✅

## Workflows connexes

- `/setup-environment` - Si environnement pas encore configuré
- `/run-jupyter` - Pour lancer Jupyter et travailler sur les notebooks
