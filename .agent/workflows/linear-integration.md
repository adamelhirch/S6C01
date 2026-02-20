---
description: Intégration Linear - Lier automatiquement branches/PRs aux stories
---

# Linear Integration

Règles d'intégration entre Linear, GitHub et le développement.

## Règle Principale

**Toute story Linear DOIT avoir ses liens GitHub (branche ET PR) dans ses ressources.**

## Actions automatiques

### 1. Après création d'une branche

Attacher le lien de la branche à la story Linear :

```json
{
  "id": "ISSUE_UUID",
  "links": [
    ...liens_existants,
    {
      "title": "Branche GitHub: {prenom}/sae-XX-description",
      "url": "https://github.com/adamelhirch/S6C01/tree/{prenom}/sae-XX-description"
    }
  ]
}
```

### 2. Quand la story est terminée

a) Créer la PR vers `main`

b) AJOUTER le lien de la PR (EN PLUS de la branche) :

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

c) Après merge, mettre en "Done"

## Format des liens

| Type | Format du titre | URL |
|------|----------------|-----|
| Branche | `Branche GitHub: nom-branche` | `https://github.com/adamelhirch/S6C01/tree/nom-branche` |
| PR | `PR #XX: Titre` | `https://github.com/adamelhirch/S6C01/pull/XX` |

## IMPORTANT

- Toujours **AJOUTER** aux liens existants, **JAMAIS** les remplacer
- Récupérer les liens existants avec `get_issue` avant de mettre à jour
- Une story doit avoir au minimum : lien branche + lien PR
