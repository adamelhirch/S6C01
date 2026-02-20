# CLAUDE.md - S6C01 Yelp Analysis

## Projet

Analyse de sentiment sur les avis Yelp (NLP/ML/Deep Learning).
BUT Informatique S6 — 2025-2026.

## Stack

Python 3.12+, Pandas, Scikit-learn, PyTorch, HuggingFace Transformers.

## Commandes de développement

Le workflow principal utilise 3 commandes slash :

| Commande | Description |
|----------|-------------|
| `/start-dev` | Prendre une story Linear, créer la branche, lier à Linear, passer en "In Progress" |
| `/finish-dev` | Créer la PR, lier à Linear, passer en "In Review" |
| `/validate-pr` | Merger la PR après validation manuelle, passer en "Done" |

### Cycle complet

```
/start-dev SAE-114  →  coder  →  /finish-dev  →  review manuelle  →  /validate-pr
```

## Conventions

### Git
- **Branches** : `adam/sae-XX-description-courte` (kebab-case)
- **Commits** : `SAE-XX Description` (commencer par l'identifiant)
- **Jamais de commit direct sur main**

### Linear
- **Équipe** : SAE6C01
- **Toujours AJOUTER les liens** (branche + PR) aux ressources de la story, JAMAIS les remplacer
- **Format lien branche** : `Branche GitHub: nom-branche`
- **Format lien PR** : `PR #XX: Titre`

### Notebooks
- 1 notebook = 1 issue = 1 critère de notation
- Numérotés de 1 à 6 par epic
- Toujours exécutables sans erreur

### Code
- Réutiliser les modules de `src/` (data_utils, text_preprocessing, features, visualization)
- Éviter le code inutile (pénalité -1pt) et le copier-coller naïf (-2pts)
- Deux tâches de prédiction : polarité (3 classes) ET score (1-5)

### Langue
- Documentation et commentaires en **français**

## Fichiers de référence

- `docs/PROJECT-PLAN.md` — Grille de notation et avancement
- `.claude/PROJECT_CONTEXT.md` — Contexte détaillé du projet
