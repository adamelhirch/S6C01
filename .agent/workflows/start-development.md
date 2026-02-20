---
description: Commencer le développement sur une story Linear
---

# Start Development

Ce workflow guide le processus complet pour prendre une story Linear et commencer à coder.

## Étapes

### 1. Récupérer une story sur Linear

Si l'utilisateur fournit un identifiant (ex: `SAE-114`), récupère la story.

Sinon, liste les issues Todo de l'équipe SAE6C01 et propose à l'utilisateur de choisir.

### 2. Mettre à jour main

```bash
git checkout main
git pull origin main
```

### 3. Créer la branche Git

Format: `adam/sae-XX-description-courte` (kebab-case)

Utilise le `gitBranchName` de l'issue Linear si disponible, sinon construis-le.

```bash
git checkout -b adam/sae-XX-description-courte
```

### 4. Lier la branche à Linear

Récupère d'abord les liens existants de l'issue, puis AJOUTE le lien de branche :

```json
{
  "id": "ISSUE_UUID",
  "links": [
    ...liens_existants,
    {
      "title": "Branche GitHub: adam/sae-XX-description",
      "url": "https://github.com/adamelhirch/S6C01/tree/adam/sae-XX-description"
    }
  ],
  "state": "In Progress"
}
```

**IMPORTANT** : Toujours AJOUTER aux liens existants, JAMAIS les remplacer.

### 5. Activer le venv

```bash
source venv/bin/activate
```

### 6. Charger le contexte

Lire les fichiers clés :
1. L'issue complète Linear (description, checklist)
2. Le notebook cible s'il existe déjà
3. `docs/PROJECT-PLAN.md` pour la grille de notation
4. Les fichiers `src/` pertinents

### 7. Confirmer

Afficher un résumé :
- Issue : SAE-XX - Titre
- Branche : adam/sae-XX-description
- Notebook cible : (si mentionné dans l'issue)
- Status Linear : In Progress ✅
- Lien branche ajouté sur Linear ✅

## Résultat attendu

- ✅ Story prise sur Linear et marquée "In Progress"
- ✅ Branche créée avec nomenclature correcte
- ✅ Lien branche ajouté dans Linear
- ✅ Venv activé
- ✅ Contexte chargé, prêt à coder

## Workflows connexes

- `/finish-development` - Quand le code est terminé
- `/setup-environment` - Si environnement pas encore configuré
