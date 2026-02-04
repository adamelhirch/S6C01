---
description: Intégration Linear - Lier automatiquement branches/PRs aux stories
---

# Workflow Linear Integration

Ce workflow définit les règles d'intégration entre Linear, GitHub et le développement.

## Règle Principale

**Toute story Linear DOIT avoir ses liens GitHub (branche ET PR) dans ses ressources.**

## Workflow Automatisé

### Quand une story est terminée

1. **Créer automatiquement la Pull Request** sur GitHub
2. **Ajouter le lien de la PR** aux ressources de la story (en plus du lien de branche existant)
3. **Mettre la story en état "In Review"** dans Linear
4. La review et le merge sont manuels (faits par toi ou tes collègues)

## Instructions pour l'IA

### 1. Après création d'une branche

Attacher automatiquement le lien de la branche à la story Linear:

```
Titre: Branche GitHub: prenom/sae-XX-description
URL: https://github.com/adamelhirch/S6C01/tree/prenom/sae-XX-description
```

Utiliser l'outil `mcp__linear-server__update_issue` avec le paramètre `links`:
```json
{
  "id": "ISSUE_ID",
  "links": [{
    "title": "Branche GitHub: prenom/sae-XX-description",
    "url": "https://github.com/adamelhirch/S6C01/tree/prenom/sae-XX-description"
  }]
}
```

### 2. Quand une story est terminée (code complet)

**AUTOMATIQUEMENT:**

a) Créer la Pull Request vers `main`:
```bash
gh pr create --title "SAE-XX: Titre de la story" --body "Description de la PR"
```

b) AJOUTER le lien de la PR aux ressources (SANS supprimer le lien de branche):
```json
{
  "id": "ISSUE_ID",
  "links": [
    {
      "title": "Branche GitHub: prenom/sae-XX-description",
      "url": "https://github.com/adamelhirch/S6C01/tree/prenom/sae-XX-description"
    },
    {
      "title": "PR #XX: Titre de la PR",
      "url": "https://github.com/adamelhirch/S6C01/pull/XX"
    }
  ]
}
```

c) Mettre la story en "In Review":
```json
{
  "id": "ISSUE_ID",
  "state": "In Review"
}
```

### 3. Lors de la création d'une story

Si tu crées une story pour du travail déjà effectué (code existant sur une branche):
- Attacher directement le lien de la branche existante
- Si une PR existe déjà, ajouter aussi son lien
- Marquer la story comme "Done" si le code est mergé

## Format des liens

| Type | Format du titre | URL |
|------|----------------|-----|
| Branche | `Branche GitHub: nom-branche` | `https://github.com/adamelhirch/S6C01/tree/nom-branche` |
| PR | `PR #XX: Titre` | `https://github.com/adamelhirch/S6C01/pull/XX` |
| Commit | `Commit: message court` | `https://github.com/adamelhirch/S6C01/commit/SHA` |

## Exemple complet

Pour la story SAE-68 sur la branche `adam/sae-68-library-shared-code`:

**Après création de branche:**
```json
{
  "id": "story-uuid",
  "links": [{
    "title": "Branche GitHub: adam/sae-68-library-shared-code",
    "url": "https://github.com/adamelhirch/S6C01/tree/adam/sae-68-library-shared-code"
  }]
}
```

**Après fin du développement (automatique):**
```json
{
  "id": "story-uuid",
  "links": [
    {
      "title": "Branche GitHub: adam/sae-68-library-shared-code",
      "url": "https://github.com/adamelhirch/S6C01/tree/adam/sae-68-library-shared-code"
    },
    {
      "title": "PR #42: SAE-68 Add shared library for code reuse",
      "url": "https://github.com/adamelhirch/S6C01/pull/42"
    }
  ],
  "state": "In Review"
}
```

## Rappel

Cette intégration permet:
- La traçabilité complète du code vers les stories (branche + PR)
- La navigation rapide depuis Linear vers GitHub
- Le suivi de l'avancement du projet
- Un workflow automatisé de review
