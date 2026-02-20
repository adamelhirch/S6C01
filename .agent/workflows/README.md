# Workflows Antigravity - S6C01

Workflows pour Antigravity, chargés automatiquement et invocables avec `/nom-du-workflow`.

## Workflows de développement

| Commande | Description |
|----------|-------------|
| `/start-development` | Prendre une story Linear, créer branche, lier à Linear, passer en "In Progress" |
| `/finish-development` | Créer PR, lier à Linear, passer en "In Review" |
| `/validate-pr` | Merger la PR après validation, passer en "Done" |

### Cycle complet

```
/start-development SAE-114  →  coder  →  /finish-development  →  review  →  /validate-pr
```

## Workflows utilitaires

| Commande | Description |
|----------|-------------|
| `/setup-environment` | Configurer Python, venv, dépendances |
| `/run-jupyter` | Lancer Jupyter Notebook |

## Intégration Linear ↔ GitHub

Voir `/linear-integration` pour les règles détaillées.

**Règle principale** : toute story doit avoir sa branche ET sa PR en ressources sur Linear.

### Actions automatiques

1. **Création de branche** → lien branche ajouté sur Linear
2. **Fin de dev** → PR créée + lien PR ajouté sur Linear + story en "In Review"
3. **Validation** → PR mergée + story en "Done"
