# 🤝 Guide de Collaboration - Projet S6C01 Yelp Analysis

**Équipe:** Adam, Ewen, Natalia, Manolo, Lotfi
**Dernière mise à jour:** 27 janvier 2026

---

## 🎯 Principe fondamental

> **Linear est LA source de vérité**
> Tout le monde consulte Linear avant de commencer, tout le monde met à jour Linear après avoir avancé.

---

## 📋 Workflow en 5 étapes

### 1️⃣ **AVANT de commencer à coder**

**Checklist quotidienne:**
```bash
☐ Ouvrir Linear (https://linear.app/sae6c01)
☐ Regarder le tableau des stories
☐ Identifier une story "Backlog" ou "Todo" sans assigné
☐ S'assigner la story (cliquer "Assign to me")
☐ Passer le status en "In Progress"
☐ Lire TOUTE la description + critères d'acceptation
☐ Vérifier qu'il n'y a pas de dépendances bloquantes
```

**⚠️ Règle d'or:** Ne jamais travailler sur une story déjà assignée à quelqu'un d'autre sans lui parler avant.

---

### 2️⃣ **PENDANT le développement**

**Organisation Git:**
```bash
# 1. Pull les dernières modifications
git pull origin main

# 2. Créer une branche avec le numéro de story Linear
git checkout -b SAE-XX-description-courte
# Exemple: git checkout -b SAE-30-setup-python

# 3. Travailler sur la story
# ... coder ...

# 4. Commits réguliers et clairs
git add .
git commit -m "SAE-XX: Description de ce qui a été fait"
# Exemple: git commit -m "SAE-30: Configuration environnement Python avec requirements.txt"
```

**Communication dans Linear:**
- **Toutes les 2h ou à chaque avancée significative**, ajouter un commentaire sur la story:
  ```
  💬 Avancement:
  - ✅ Fait: [ce qui est terminé]
  - 🚧 En cours: [ce sur quoi tu bosses]
  - ⚠️ Bloqué: [problème rencontré si applicable]
  ```

**Exemple concret:**
```markdown
💬 Avancement SAE-30:
- ✅ Python 3.11 installé
- ✅ requirements.txt créé avec pandas, scikit-learn
- 🚧 Test du chargement des JSON Yelp
- ⚠️ Le fichier reviews.json est corrompu ligne 1247 - besoin d'aide
```

---

### 3️⃣ **QUAND tu as un problème**

**Ne reste JAMAIS bloqué plus de 30 minutes sans demander de l'aide!**

```markdown
Option 1: Dans le commentaire Linear
@equipe Besoin d'aide sur [problème précis]

Option 2: Discord/groupe WhatsApp
"Check SAE-XX sur Linear, je suis bloqué sur [problème]"

Option 3: Demander à Claude (moi!)
"Claude, aide-moi sur SAE-XX"
→ Je vais automatiquement consulter Linear, lire la story, et t'aider
```

---

### 4️⃣ **QUAND tu as terminé**

**Checklist avant de marquer "Done":**
```bash
☐ Le code fonctionne (testé localement)
☐ Le code est commenté (seulement si nécessaire)
☐ Tous les critères d'acceptation sont ✅
☐ Le notebook est sauvegardé et exécutable
☐ Les fichiers sont commitées
```

**Process de finalisation:**
```bash
# 1. Push ta branche
git push origin SAE-XX-description-courte

# 2. Créer une Pull Request (PR) sur GitHub
# - Titre: "SAE-XX: Description"
# - Description: Copier les critères d'acceptation de Linear
# - Mentionner: "Closes SAE-XX" (pour lier à Linear)

# 3. Dans Linear:
# - Ajouter le lien de la PR dans un commentaire
# - NE PAS encore passer en "Done"

# 4. Attendre la review d'un autre membre de l'équipe
# - Quelqu'un d'autre doit tester ton code
# - Il commente dans la PR: "LGTM" (Looks Good To Me) ou demande des modifs

# 5. Merger la PR
# - Soit toi après approbation
# - Soit le reviewer

# 6. MAINTENANT passer la story Linear en "Done"
# - Status: Done
# - Commentaire final: "✅ Mergé dans main via PR #XX"
```

---

### 5️⃣ **COORDINATION d'équipe**

**Réunions rapides (15 min max):**
- **Lundi matin:** Qui prend quoi cette semaine?
- **Mercredi midi:** Point d'avancement, problèmes?
- **Vendredi soir:** Ce qui est fait, ce qui reste

**Répartition équitable:**
```
Chaque Epic = 5 stories
Chaque membre = ~5-6 stories au total
```

**Suggestion de répartition par compétences:**
```
📊 Data/Stats → Qui est à l'aise avec pandas/numpy?
🤖 ML/NLP → Qui connaît scikit-learn?
💻 LLM/HuggingFace → Qui a déjà utilisé des transformers?
📈 Dataviz → Qui fait de beaux graphiques?
📝 Documentation → Qui écrit bien en français?
```

**⚠️ Important:** Ce n'est pas rigide! On peut s'entraider et switcher.

---

## 🚨 Résolution de conflits

### Conflit Git (merge conflict)

**Si tu as un conflit lors du pull:**
```bash
# 1. Identifier les fichiers en conflit
git status

# 2. Ouvrir le fichier, tu verras:
<<<<<<< HEAD
Ton code
=======
Code de l'autre
>>>>>>> branch-name

# 3. Décider quoi garder:
# - Soit ton code
# - Soit le code de l'autre
# - Soit une fusion des deux

# 4. Supprimer les marqueurs (<<<<, ====, >>>>)

# 5. Committer la résolution
git add fichier-resolu.py
git commit -m "Résolution conflit avec [nom-branche]"
```

**💡 Prévention:** Communiquer dans Linear sur quels fichiers vous bossez!

---

### Conflit de tâches (deux personnes sur la même chose)

```markdown
Scénario: Adam et Ewen bossent tous les deux sur SAE-35 (preprocessing)

Solution:
1. Le premier qui a commencé continue
2. Le deuxième prend la story suivante
3. OU split la story en 2 sous-tâches:
   - SAE-35a: Tokenization (Adam)
   - SAE-35b: Stopwords removal (Ewen)

→ Créer les sous-stories dans Linear avec @mention
```

---

## 📊 Dashboard Linear - Comment l'utiliser

**Vues utiles:**

1. **Vue "My Issues"**: Tes stories en cours
2. **Vue "Team"**: Voir qui fait quoi
3. **Vue "Backlog"**: Stories disponibles à prendre
4. **Vue "Epic X"**: Toutes les stories d'un Epic

**Filtres utiles:**
```
Status = "In Progress" → Voir ce qui est en cours
Assignee = "Unassigned" → Trouver une story à prendre
Priority = "Urgent" → Les stories bloquantes (SAE-55, SAE-57)
```

---

## 🎓 Bonnes pratiques spécifiques DATA/ML

### 1. **Notebooks Jupyter**

```bash
Structure conseillée:
notebooks/
├── epic1-setup/
│   ├── SAE-30-setup-env.ipynb
│   ├── SAE-31-load-data.ipynb
├── epic2-text-rep/
│   ├── SAE-35-preprocessing.ipynb
│   ├── SAE-36-tfidf.ipynb
└── ...

Règles:
- 1 notebook = 1 story
- Nom du fichier = SAE-XX-description.ipynb
- Toujours mettre un titre markdown au début
- Toujours "Restart & Run All" avant de commit
```

### 2. **Données**

```bash
⚠️ NE JAMAIS commit les données brutes (fichiers JSON volumineux)

Dans .gitignore:
data/*.json
data/*.csv

Par contre, COMMIT:
- data/sample-10-reviews.json (petit échantillon pour tests)
- data/README.md (description des fichiers)
```

### 3. **Environnement Python**

```bash
requirements.txt TOUJOURS à jour:

# Chaque fois que tu installes un package:
pip install nouvelle-library
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add nouvelle-library to requirements"

# Les autres peuvent ensuite faire:
pip install -r requirements.txt
```

### 4. **Résultats et outputs**

```bash
outputs/
├── epic2-embeddings/
│   ├── tfidf-matrix.pkl
│   ├── word2vec-model.bin
├── epic3-ml/
│   ├── logistic-regression-model.pkl
│   ├── classification-report.txt
└── ...

✅ COMMIT les petits fichiers (.txt, .png)
❌ NE PAS COMMIT les gros modèles (.pkl > 100MB)
→ Utiliser Git LFS ou les exclure dans .gitignore
```

---

## 🤖 Travailler avec Claude (moi!)

**Je suis configuré pour suivre Linear. Voici comment m'utiliser efficacement:**

### Commande type:
```
"Claude, aide-moi sur SAE-36"

→ Je vais automatiquement:
1. Lister les stories pour voir l'état du projet
2. Lire SAE-36 en détail (description, critères, commentaires)
3. T'aider avec le code
4. Ajouter un commentaire dans Linear avec ce qu'on a fait
5. Suggérer de mettre à jour le status si c'est terminé
```

### Exemples de requêtes:
```
✅ "Claude, aide-moi sur SAE-36, j'ai une erreur avec TfidfVectorizer"
✅ "Claude, montre-moi comment faire SAE-40 (Logistic Regression)"
✅ "Claude, révise mon code pour SAE-35 avant que je push"
✅ "Claude, où en est le projet? Qu'est-ce qui est bloqué?"

❌ "Claude, fais SAE-36 pour moi" (Je t'aide, je ne fais pas à ta place!)
```

### Workflow de collaboration avec moi:
```
1. Tu commences une story
2. Tu bloques sur quelque chose
3. "Claude, aide-moi sur SAE-XX, [problème]"
4. On résout ensemble
5. Je documente dans Linear via un commentaire
6. Tu continues, tu termines
7. Tu marques la story Done
```

---

## ⏰ Planning type (exemple semaine)

**Semaine du 27 jan - 2 fév (Epic 1):**

```
Lundi 27/01:
- Réunion 30 min: Répartition des stories Epic 1
- Adam → SAE-55 (GitHub repo)
- Ewen → SAE-57 (Linear config)
- Natalia → SAE-30 (Setup Python)
- Manolo → SAE-31 (Load data)
- Lotfi → SAE-32 (EDA)

Mercredi 29/01:
- Point rapide Discord 15 min
- Vérifier avancement, problèmes?
- Ajuster si besoin

Vendredi 31/01:
- Review collective 1h
- Merger les PRs
- Préparer Epic 2 pour la semaine suivante
```

---

## 📞 Communication d'urgence

**Niveaux de communication:**

🟢 **Pas urgent** (réponse sous 24h)
→ Commentaire dans Linear

🟡 **Important** (réponse sous 4h)
→ Discord/WhatsApp + tag @equipe dans Linear

🔴 **Bloquant** (réponse immédiate)
→ Appel Discord vocal + message direct à Adam (chef de projet)

**Exemples:**
- 🟢 "J'ai optimisé le code de preprocessing"
- 🟡 "Mon notebook crash, j'ai essayé 3 solutions, rien ne marche"
- 🔴 "Le repo GitHub a disparu" / "On rend demain et rien ne marche"

---

## ✅ Checklist finale avant rendu

**2 jours avant le rendu:**
```bash
☐ Toutes les stories Epic 1-5 sont "Done" dans Linear
☐ Toutes les branches sont mergées dans main
☐ Le notebook final s'exécute end-to-end sans erreur
☐ README.md est complet et à jour
☐ requirements.txt fonctionne (testé sur machine propre)
☐ Rapport technique écrit (SAE-52)
☐ Présentation orale préparée (SAE-53)
☐ Démo répétée au moins 1 fois
☐ Tous les membres savent présenter leur partie
```

---

## 🎉 Philosophie de l'équipe

> **1. Communication > Code**
> Un bug signalé vaut mieux qu'un bug caché.

> **2. Entraide > Performance individuelle**
> Si quelqu'un est bloqué, on l'aide. Point.

> **3. Documentation > Mémoire**
> Linear + GitHub = notre mémoire collective.

> **4. Itération > Perfection**
> Version fonctionnelle imparfaite > Version parfaite jamais finie.

> **5. Transparence > Ego**
> "Je ne comprends pas" est une phrase puissante.

---

## 🆘 FAQ - Questions fréquentes

**Q: J'ai oublié de créer une branche, j'ai commit directement sur main!**
R: Pas de panique. `git log` pour voir ton commit, `git revert` si besoin, ou demande à Adam/Claude.

**Q: Mon notebook fait 500 lignes, c'est normal?**
R: Non. Split en plusieurs notebooks par story. 1 story = 1 notebook de 50-150 lignes max.

**Q: Je ne trouve pas de story disponible dans mon Epic.**
R: Regarde les autres Epics, ou demande à l'équipe si quelqu'un veut de l'aide sur sa story.

**Q: Ewen a écrit du code incompréhensible, je fais quoi?**
R: Tag @ewen dans Linear: "Peux-tu expliquer cette partie?" + review de code bienveillante.

**Q: On est vendredi soir, 3 stories sont en retard.**
R: Réunion d'urgence. Soit on parallélise (2 personnes par story), soit on priorise et on coupe ce qui est moins critique.

**Q: Claude ne comprend pas ma question.**
R: Reformule avec le numéro de story: "Claude, sur SAE-36, comment vectoriser avec TF-IDF?"

---

## 📚 Ressources

**Linear:** https://linear.app/sae6c01
**GitHub:** [Lien du repo une fois SAE-55 terminé]
**Discord équipe:** [Votre serveur]
**Google Drive (si utilisé):** [Lien]

**Documentation technique:**
- Scikit-learn: https://scikit-learn.org/stable/
- Gensim (Word2Vec): https://radimrehurek.com/gensim/
- HuggingFace Transformers: https://huggingface.co/docs/transformers/

---

## 🔄 Mise à jour de ce guide

**Ce guide est vivant!** Si vous trouvez une meilleure façon de faire, mettez-le à jour:

```bash
git checkout -b update-guide
# Modifier GUIDE-COLLABORATION.md
git commit -m "Amélioration du guide: [description]"
git push origin update-guide
# Créer PR, demander review, merger
```

---

**Version:** 1.0
**Auteurs:** Adam + Claude
**Dernière révision:** 27 janvier 2026

**Let's go team! 🚀**
