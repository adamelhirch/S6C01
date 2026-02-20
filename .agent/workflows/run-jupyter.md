---
description: Lancer Jupyter et travailler avec les notebooks
---

# Lancer Jupyter Notebook

## Étapes

### 1. Activer le venv

```bash
source venv/bin/activate
```

### 2. Lancer Jupyter

```bash
jupyter notebook
```

Accessible sur `http://localhost:8888`

### 3. Structure des notebooks

```
notebooks/
├── 1-data-loading/          ✅ Done
├── 2-preprocessing/         ✅ Done
├── 3-text-representation/   ✅ Done (+SAE-112)
├── 4-ml-classique/          ⬜ SAE-114, 116, 117, 118
├── 5-deep-learning/         ⬜ SAE-113, 115, 119, 124
└── 6-inference/             ⬜ SAE-120, 121
```

### 4. Première cellule d'un nouveau notebook

```python
# Epic X - Story SAE-XX - Titre
# Auteur: Prénom NOM
# Date: YYYY-MM-DD

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8-darkgrid')
```

## Tips

- **Restart kernel** : si un notebook freeze
- **Clear outputs** : avant de commiter (`Cell → All Output → Clear`)
- 1 notebook = 1 issue = 1 critère de notation
