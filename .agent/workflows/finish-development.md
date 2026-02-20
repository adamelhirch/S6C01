---
description: Terminer le développement et créer une PR
---

# Finish Development

Le développement sur la story est terminé. Créer une Pull Request et lier à Linear.

## Étapes

### 1. Identifier la story en cours

Déterminer l'issue à partir de la branche actuelle :

```bash
git branch --show-current
```

Le format est `{prenom}/sae-XX-description` → extraire `SAE-XX`.

Récupérer l'issue complète sur Linear.

### 2. Vérifier les changements

```bash
git status
git diff --stat
```

S'il y a des fichiers non commités, les commiter avec le format :
```
SAE-XX Description du travail

- Détail 1
- Détail 2
```

### 3. Pousser la branche

```bash
git push -u origin NOM_BRANCHE
```

### 4. Créer la Pull Request

- **Repo**: adamelhirch/S6C01
- **Title**: `SAE-XX: Titre de la story`
- **Head**: nom de la branche
- **Base**: main
- **Body**: Résumé des changements + lien vers la story Linear + critères de notation concernés

### 5. Lier la PR à Linear

Récupérer les liens existants, puis AJOUTER le lien de la PR :

```json
{
  "id": "ISSUE_UUID",
  "links": [
    ...liens_existants,
    {
      "title": "PR #XX: SAE-XX Titre",
      "url": "https://github.com/adamelhirch/S6C01/pull/XX"
    }
  ],
  "state": "In Review"
}
```

**IMPORTANT** : Toujours AJOUTER aux liens existants, JAMAIS les remplacer.

### 6. Confirmer

Afficher un résumé :
- PR créée : #XX — lien direct
- Story Linear : SAE-XX passée en "In Review" ✅
- Lien PR ajouté sur Linear ✅
- Prochaine étape : review manuelle, puis `/validate-pr` pour merger

## Résultat attendu

- ✅ Tous les changements commités et poussés
- ✅ PR créée sur GitHub
- ✅ Lien PR ajouté dans Linear (sans écraser la branche)
- ✅ Story en "In Review"
