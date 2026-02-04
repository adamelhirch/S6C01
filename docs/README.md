# Documentation S6C01

Ce dossier contient toute la documentation du projet pour l'équipe et les assistants IA.

## Pour les humains (Guides complets)

Ces guides sont conçus pour les utilisateurs de claude-cli ou ceux qui travaillent manuellement:

### Setup et Configuration
- **[WORKFLOW_SETUP.md](WORKFLOW_SETUP.md)** - Configuration environnement Python, venv, dépendances

### Développement
- **[WORKFLOW_DEVELOPMENT.md](WORKFLOW_DEVELOPMENT.md)** - Workflow Git complet (11 étapes de A à Z)
- **[WORKFLOW_JUPYTER.md](WORKFLOW_JUPYTER.md)** - Lancer Jupyter, créer notebooks, bonnes pratiques
- **[WORKFLOW_DATA_PIPELINE.md](WORKFLOW_DATA_PIPELINE.md)** - Pipeline données (JSON → Parquet)

### Intégration
- **[WORKFLOW_LINEAR_INTEGRATION.md](WORKFLOW_LINEAR_INTEGRATION.md)** - Intégration Linear ↔ GitHub (manuel et automatique)

### Référence
- **[AI_INSTRUCTIONS.md](AI_INSTRUCTIONS.md)** - Conventions de code, patterns, templates
- **[PROJECT-PLAN.md](PROJECT-PLAN.md)** - Plan complet du projet (Epics, Stories, Timeline)
- **[QUICKSTART.md](QUICKSTART.md)** - Guide démarrage rapide (onboarding)

## Pour les IA

Les assistants IA doivent consulter en priorité:

1. **[`../.claude/PROJECT_CONTEXT.md`](../.claude/PROJECT_CONTEXT.md)** - Contexte complet, chargé automatiquement
2. **[`../.agent/workflows/`](../.agent/workflows/)** - Workflows Antigravity
3. **[AI_INSTRUCTIONS.md](AI_INSTRUCTIONS.md)** - Conventions et patterns de code

## Structure de la documentation

```
docs/
├── README.md                          # Ce fichier
│
├── WORKFLOW_*.md                      # Guides pratiques pour humains
│   ├── WORKFLOW_SETUP.md              # Setup environnement
│   ├── WORKFLOW_DEVELOPMENT.md        # Workflow Git complet
│   ├── WORKFLOW_JUPYTER.md            # Travailler avec Jupyter
│   ├── WORKFLOW_DATA_PIPELINE.md      # Pipeline de données
│   └── WORKFLOW_LINEAR_INTEGRATION.md # Intégration Linear ↔ GitHub
│
├── AI_INSTRUCTIONS.md                 # Instructions pour IA (conventions)
├── PROJECT-PLAN.md                    # Plan du projet (Epics/Stories)
├── QUICKSTART.md                      # Guide démarrage rapide
│
└── stories/                           # Documentation par story
    └── (fichiers créés au fur et à mesure)
```

## Différence Workflows vs AI Instructions

**`WORKFLOW_*.md`** (dans `docs/`)
- Guides détaillés pour humains
- Instructions pas-à-pas
- Commandes à copier-coller
- Troubleshooting
- Checklist

**`../.agent/workflows/*.md`** (workflows Antigravity)
- Instructions concises pour Antigravity
- Commandes à exécuter automatiquement
- Format workflow avec frontmatter
- Chargés automatiquement par Antigravity

**`../.claude/PROJECT_CONTEXT.md`** (contexte IA)
- Contexte complet du projet
- Chargé automatiquement par toutes les IA
- Instructions MCP Linear/GitHub
- Workflow automatisé

## Comment utiliser cette documentation

### Si tu es un membre de l'équipe (humain):

1. **Premier jour?** → Lis [QUICKSTART.md](QUICKSTART.md)
2. **Setup environnement?** → [WORKFLOW_SETUP.md](WORKFLOW_SETUP.md)
3. **Prêt à coder?** → [WORKFLOW_DEVELOPMENT.md](WORKFLOW_DEVELOPMENT.md)
4. **Besoin de Jupyter?** → [WORKFLOW_JUPYTER.md](WORKFLOW_JUPYTER.md)
5. **Intégration Linear?** → [WORKFLOW_LINEAR_INTEGRATION.md](WORKFLOW_LINEAR_INTEGRATION.md)
6. **Conventions de code?** → [AI_INSTRUCTIONS.md](AI_INSTRUCTIONS.md)

### Si tu es une IA (Antigravity, claude-cli):

1. **Charge automatiquement:** [`../.claude/PROJECT_CONTEXT.md`](../.claude/PROJECT_CONTEXT.md)
2. **Consulte:** [AI_INSTRUCTIONS.md](AI_INSTRUCTIONS.md) pour les conventions
3. **Utilise:** Les outils MCP Linear et GitHub pour automatiser
4. **Référence:** Les workflows dans `../.agent/workflows/` si nécessaire

## Maintenir la documentation

### Quand ajouter de la doc?

- **Nouveau workflow?** → Crée `WORKFLOW_NOM.md` dans `docs/`
- **Nouvelle convention?** → Mets à jour `AI_INSTRUCTIONS.md`
- **Changement de process?** → Mets à jour `PROJECT_CONTEXT.md`
- **Story terminée?** → Documente dans `stories/SAE-XX.md` si nécessaire

### Format recommandé

Utilise le même format que les fichiers existants:
- Titres clairs
- Exemples de code avec syntaxe highlighting
- Checklist quand applicable
- Liens vers autres docs
- Section "Problèmes courants"

## Questions?

Consulte d'abord cette documentation. Si tu ne trouves pas la réponse:
- Linear: https://linear.app/sae6c01
- GitHub: https://github.com/adamelhirch/S6C01
- Discord de l'équipe
