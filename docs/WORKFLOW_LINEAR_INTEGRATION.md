# Guide Intégration Linear ↔ GitHub

**Pour utilisateurs claude-cli et développement manuel**

## Vue d'ensemble

Ce guide explique comment Linear et GitHub sont intégrés dans ce projet, et comment utiliser cette intégration efficacement.

## Principe de base

**Règle:** Chaque story Linear doit avoir des liens vers ses ressources GitHub (branche ET Pull Request).

## Workflow automatisé (avec Antigravity)

Si vous utilisez Antigravity, l'intégration est automatique:

1. **Création de branche** → Lien branche ajouté automatiquement à la story
2. **Story terminée** → PR créée automatiquement + lien PR ajouté + story en "In Review"
3. **PR mergée** → Story passée en "Done"

## Workflow manuel (avec claude-cli ou sans IA)

Si vous n'utilisez pas Antigravity, vous devez ajouter les liens manuellement.

### Étape 1: Ajouter le lien de branche

**Quand:** Juste après avoir créé votre branche Git

**Comment:**
1. Aller sur votre story Linear
2. Dans la section "Resources" (ou "Links")
3. Cliquer "Add link"
4. Remplir:
   - **Title:** `Branche GitHub: prenom/sae-XX-description`
   - **URL:** `https://github.com/adamelhirch/S6C01/tree/prenom/sae-XX-description`
5. Sauvegarder

**Exemple:**
- Title: `Branche GitHub: adam/sae-68-shared-library`
- URL: `https://github.com/adamelhirch/S6C01/tree/adam/sae-68-shared-library`

### Étape 2: Ajouter le lien de Pull Request

**Quand:** Juste après avoir créé votre PR sur GitHub

**Comment:**
1. Copier l'URL de votre PR (ex: `https://github.com/adamelhirch/S6C01/pull/42`)
2. Aller sur votre story Linear
3. Dans la section "Resources" (ou "Links")
4. Cliquer "Add link"
5. Remplir:
   - **Title:** `PR #XX: Titre de la PR`
   - **URL:** L'URL copiée
6. Sauvegarder

**Exemple:**
- Title: `PR #42: SAE-68 Add shared library`
- URL: `https://github.com/adamelhirch/S6C01/pull/42`

### Étape 3: Mettre la story en "In Review"

**Quand:** Après avoir créé la PR

**Comment:**
1. Dans Linear, glisser la story vers "In Review"
2. Ou cliquer sur le status et sélectionner "In Review"

### Étape 4: Merger et finaliser

**Quand:** Après approbation de la PR

1. Merger la PR sur GitHub
2. Dans Linear, glisser la story vers "Done"

## Format des liens

| Type | Format du titre | Exemple URL |
|------|----------------|-------------|
| Branche | `Branche GitHub: nom-branche` | `https://github.com/adamelhirch/S6C01/tree/adam/sae-68-lib` |
| PR | `PR #XX: Titre` | `https://github.com/adamelhirch/S6C01/pull/42` |

## Exemple complet

### Story SAE-68: Ajouter shared library

**Étape 1: Création de branche**
```bash
git checkout -b adam/sae-68-shared-library
git push -u origin adam/sae-68-shared-library
```

→ Ajouter dans Linear:
- Title: `Branche GitHub: adam/sae-68-shared-library`
- URL: `https://github.com/adamelhirch/S6C01/tree/adam/sae-68-shared-library`

**Étape 2: Développement**
```bash
# Coder...
git add .
git commit -m "SAE-68 Add shared library"
git push
```

**Étape 3: Création de PR**
```bash
gh pr create --title "SAE-68 Add shared library" --body "Description"
```

→ Ajouter dans Linear:
- Title: `PR #42: SAE-68 Add shared library`
- URL: `https://github.com/adamelhirch/S6C01/pull/42`

→ Mettre la story en "In Review"

**Étape 4: Review et merge**

Après approbation:
```bash
gh pr merge 42
```

→ Mettre la story en "Done"

## Avantages de cette intégration

### Traçabilité complète

Depuis Linear, vous pouvez:
- Voir la branche associée à la story
- Voir la PR et les reviews
- Naviguer rapidement vers GitHub

### Contexte pour les reviews

Les reviewers peuvent:
- Voir la story Linear pour comprendre le contexte
- Vérifier que le code répond bien aux critères d'acceptation

### Suivi de l'avancement

L'équipe peut:
- Voir l'état de chaque story
- Identifier les PRs en attente de review
- Suivre ce qui est mergé

## Automatiser avec GitHub CLI

Si vous utilisez `gh` (GitHub CLI), vous pouvez automatiser partiellement:

### Créer une PR avec lien vers Linear

```bash
gh pr create \
  --title "SAE-68 Add shared library" \
  --body "Closes SAE-68

Description des changements...

Linear story: https://linear.app/sae6c01/issue/SAE-68"
```

### Ajouter un commentaire sur la PR depuis Linear

Dans Linear, vous pouvez ajouter l'URL de la PR dans un commentaire:

```
PR créée: https://github.com/adamelhirch/S6C01/pull/42
Prêt pour review @natalia @ewen
```

## Intégration bidirectionnelle (future)

Linear propose des intégrations GitHub natives qui peuvent:

1. **Automatiquement créer des branches** depuis Linear
2. **Synchroniser les statuts** (PR merged → Story Done)
3. **Lier automatiquement** les PRs aux stories si le titre contient "SAE-XX"

Pour activer cette intégration (admin uniquement):
1. Linear → Settings → Integrations
2. Ajouter GitHub integration
3. Configurer les règles de synchronisation

## Checklist pour chaque story

**Lors de la création de branche:**
- [ ] Branche créée avec nomenclature correcte
- [ ] Branche poussée sur GitHub
- [ ] Lien branche ajouté dans Linear
- [ ] Story en "In Progress"

**Lors de la création de PR:**
- [ ] PR créée avec titre formaté (SAE-XX)
- [ ] Lien PR ajouté dans Linear (en plus du lien branche)
- [ ] Story mise en "In Review"
- [ ] Reviewers assignés

**Après le merge:**
- [ ] PR mergée sur GitHub
- [ ] Story mise en "Done" dans Linear
- [ ] Branche locale supprimée

## Pour les admins/leads du projet

### Configuration de l'intégration Linear ↔ GitHub

Si vous voulez automatiser complètement:

1. Dans Linear: Settings → Integrations → GitHub
2. Connecter le repository `adamelhirch/S6C01`
3. Configurer les règles:
   - Créer branche depuis Linear
   - Auto-close story quand PR mergée
   - Synchroniser labels

### Webhooks (optionnel)

Pour une intégration plus poussée, vous pouvez configurer des webhooks qui:
- Créent automatiquement des PRs quand une story passe en "In Review"
- Synchronisent les commentaires entre Linear et GitHub
- Notifient sur Slack/Discord

## Problèmes courants

### Lien de branche ne fonctionne pas (404)

**Cause:** La branche n'a pas été poussée sur GitHub

**Solution:**
```bash
git push -u origin nom-de-votre-branche
```

### PR non liée à la story

**Cause:** Le lien n'a pas été ajouté manuellement

**Solution:** Ajouter le lien manuellement dans Linear (voir Étape 2 ci-dessus)

### Story pas mise à jour après merge

**Cause:** Pas d'intégration automatique configurée

**Solution:** Mettre la story en "Done" manuellement

## Ressources

- [Linear GitHub Integration](https://linear.app/docs/github)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
- Documentation interne: `WORKFLOW_DEVELOPMENT.md`

## Conseils finaux

### Pour les utilisateurs claude-cli

Demandez à Claude de vous aider à:
- Formatter les messages de commit
- Créer les liens Linear avec les bonnes URLs
- Rédiger les descriptions de PR

### Pour les utilisateurs Antigravity

Profitez de l'automatisation complète! Vous n'avez qu'à dire "termine la story" et tout le reste se fait automatiquement.

### Pour tous

La traçabilité est essentielle pour le travail d'équipe. Prenez 30 secondes pour ajouter les liens, ça facilitera grandement la collaboration!
