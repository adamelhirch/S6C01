# Workflows Antigravity - S6C01

Ce dossier contient les workflows pour Antigravity. Ces workflows sont automatiquement chargés et peuvent être invoqués avec `/nom-du-workflow`.

## Workflows disponibles

### `/linear-integration`
**Description:** Intégration automatique Linear ↔ GitHub

**Ce workflow fait:**
- Ajoute automatiquement les liens de branche dans Linear
- Crée la PR quand la story est terminée
- Ajoute le lien de PR dans Linear
- Met la story en "In Review"

**Utilisation:**
- Automatique quand tu travailles sur une story
- Pas besoin de l'invoquer manuellement

### `/setup-environment`
**Description:** Configure l'environnement Python

**Ce workflow fait:**
- Crée le venv
- Installe les dépendances
- Télécharge les ressources NLTK

**Utilisation:**
```
/setup-environment
```

### `/start-development`
**Description:** Commence une nouvelle story

**Ce workflow fait:**
- Récupère une story Linear
- Crée la branche Git
- Ajoute le lien dans Linear
- Active le venv

**Utilisation:**
```
/start-development
```

### `/run-jupyter`
**Description:** Lance Jupyter Notebook

**Ce workflow fait:**
- Active le venv
- Lance Jupyter
- Ouvre le navigateur

**Utilisation:**
```
/run-jupyter
```

### `/data-pipeline`
**Description:** Exécute le pipeline de données

**Ce workflow fait:**
- Charge les JSON
- Nettoie les données
- Exporte en Parquet

**Utilisation:**
```
/data-pipeline
```

## Comment ça marche

Les workflows sont des fichiers markdown avec frontmatter:

```markdown
---
description: Description courte du workflow
---

# Titre du Workflow

Instructions détaillées...
```

Antigravity les lit automatiquement au démarrage et peut les exécuter quand nécessaire.

## Workflow Linear-GitHub (Automatique)

### Règle principale

**Toute story Linear DOIT avoir des liens vers sa branche ET sa PR dans ses ressources.**

### Actions automatiques

#### 1. Après création de branche
```json
{
  "id": "ISSUE_ID",
  "links": [{
    "title": "Branche GitHub: prenom/sae-XX-description",
    "url": "https://github.com/adamelhirch/S6C01/tree/prenom/sae-XX-description"
  }]
}
```

#### 2. Quand story terminée

**a) Créer la PR:**
```bash
gh pr create --title "SAE-XX: Titre" --body "Description"
```

**b) Ajouter lien PR (EN PLUS de la branche):**
```json
{
  "id": "ISSUE_ID",
  "links": [
    {
      "title": "Branche GitHub: prenom/sae-XX-description",
      "url": "https://github.com/adamelhirch/S6C01/tree/prenom/sae-XX-description"
    },
    {
      "title": "PR #XX: Titre",
      "url": "https://github.com/adamelhirch/S6C01/pull/XX"
    }
  ]
}
```

**c) Mettre en Review:**
```json
{
  "id": "ISSUE_ID",
  "state": "In Review"
}
```

## Pour les développeurs

Si tu veux ajouter un nouveau workflow:

1. Crée un fichier `.md` dans ce dossier
2. Ajoute le frontmatter avec `description`
3. Écris les instructions en markdown
4. Antigravity le chargera automatiquement au prochain démarrage
