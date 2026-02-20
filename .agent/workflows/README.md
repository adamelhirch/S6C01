# Workflows .agent - S6C01

Workflows partagés pour toute l'équipe, chargés automatiquement.

## Commandes de développement

| Commande | Description |
|----------|-------------|
| `start-development` | Prendre une story Linear, créer branche, lier à Linear, passer en "In Progress" |
| `finish-development` | Créer PR, lier à Linear, passer en "In Review" |
| `validate-pr` | Merger la PR après validation, passer en "Done" |

### Cycle complet

```
start-development SAE-114  →  coder  →  finish-development  →  review  →  validate-pr
```

## Workflows utilitaires

| Commande | Description |
|----------|-------------|
| `setup-environment` | Configurer Python, venv, dépendances |
| `run-jupyter` | Lancer Jupyter Notebook |

## Intégration Linear ↔ GitHub

Voir `linear-integration.md` pour les règles détaillées.

**Règle principale** : toute story doit avoir sa branche ET sa PR en ressources sur Linear.

## Détection automatique de l'utilisateur

Les workflows détectent le développeur via `git config user.name` et extraient le prénom en minuscules pour nommer les branches : `{prenom}/sae-XX-description`.
