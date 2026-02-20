---
description: Valider et merger une PR après review
---

# Validate PR

L'utilisateur a validé la PR. Merger et mettre à jour Linear.

## Étapes

### 1. Identifier la PR

Si l'utilisateur donne un numéro de PR, l'utiliser.

Sinon, déterminer à partir de la branche actuelle et lister les PRs ouvertes.

### 2. Vérifier l'état de la PR

Vérifier :
- La PR est bien ouverte
- Pas de conflits avec main

Si conflits, prévenir l'utilisateur et proposer de résoudre.

### 3. Merger la PR

- **Repo**: adamelhirch/S6C01
- **Merge method**: squash (historique propre)

### 4. Mettre à jour Linear

Extraire l'identifiant SAE-XX depuis le titre de la PR ou la branche.

Mettre la story en "Done".

### 5. Nettoyer

```bash
git checkout main
git pull origin main
git branch -d NOM_BRANCHE_LOCALE
```

### 6. Confirmer

Afficher un résumé :
- PR #XX mergée ✅
- Story SAE-XX passée en "Done" ✅
- Branche locale supprimée ✅
- Sur `main` à jour

Proposer de continuer avec `/start-development` pour la prochaine story.

## Résultat attendu

- ✅ PR mergée sur main
- ✅ Story Linear en "Done"
- ✅ Branche nettoyée
- ✅ Prêt pour la prochaine story
