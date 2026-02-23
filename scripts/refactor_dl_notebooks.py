"""Script de génération des notebooks DL refactorisés (Phase 3)."""
import nbformat as nbf

def md(source):
    return nbf.v4.new_markdown_cell(source)

def code(source):
    return nbf.v4.new_code_cell(source)

def save_nb(cells, path):
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata['kernelspec'] = {
        'display_name': 'Python 3', 'language': 'python', 'name': 'python3'
    }
    with open(path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f'  ✓ {path}')


# ============================================================
# 01-deep-tfidf.ipynb — MLP PyTorch sur TF-IDF
# ============================================================
def gen_01():
    return [
        md("""# Deep Learning sur TF-IDF — MLP (Multi-Layer Perceptron)

MLP PyTorch sur features TF-IDF pour la classification de sentiment Yelp.

**Architecture** : Input(10000) → Dense(256) → ReLU → Dropout → Dense(128) → ReLU → Dropout → Output

**Deux tâches** : Polarité (3 classes) et Score (1-5 étoiles)"""),

        code("""import sys
sys.path.insert(0, '../..')

import os
import pandas as pd
import torch
import torch.nn as nn
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings('ignore')

from src.constants import POLARITY_NAMES, SCORE_NAMES
from src.ml_utils import load_and_prepare, split_data
from src.dl_utils import get_device, set_seed, make_loaders, train_model, evaluate_model
from src.evaluation import plot_confusion, plot_training_curves, print_report
from src import setup_plot_style

setup_plot_style()
set_seed()
device = get_device()
MODELS_DIR = '../../models'
os.makedirs(MODELS_DIR, exist_ok=True)
print(f"Device : {device}")"""),

        md("## 1. Chargement et Préparation"),

        code("""df = load_and_prepare()
data = split_data(df['text'], df['polarity'], df['stars'])
print(f"Train: {len(data['X_train'])} | Val: {len(data['X_val'])} | Test: {len(data['X_test'])}")"""),

        md("## 2. Vectorisation TF-IDF"),

        code("""vectorizer = TfidfVectorizer(max_features=10_000, min_df=5, max_df=0.7, ngram_range=(1, 2))

X_train = vectorizer.fit_transform(data['X_train']).toarray()
X_val = vectorizer.transform(data['X_val']).toarray()
X_test = vectorizer.transform(data['X_test']).toarray()

# Score 0-indexed pour PyTorch (1-5 → 0-4)
y_sc_train = (data['y_sc_train'] - 1).values.astype(int)
y_sc_val = (data['y_sc_val'] - 1).values.astype(int)
y_sc_test = (data['y_sc_test'] - 1).values.astype(int)

print(f"Dimension TF-IDF : {X_train.shape[1]} features")"""),

        md("## 3. Architecture MLP"),

        code("""class MLP(nn.Module):
    def __init__(self, input_dim, num_classes, dropout=0.3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 256), nn.ReLU(), nn.Dropout(dropout),
            nn.Linear(256, 128), nn.ReLU(), nn.Dropout(dropout),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        return self.net(x)

model_test = MLP(X_train.shape[1], 3)
print(model_test)
print(f"\\nParamètres : {sum(p.numel() for p in model_test.parameters()):,}")
del model_test"""),

        md("## 4. Polarité (3 classes)"),

        code("""train_pol, val_pol, test_pol = make_loaders(
    X_train, data['y_pol_train'].values,
    X_val, data['y_pol_val'].values,
    X_test, data['y_pol_test'].values
)

model_pol = MLP(X_train.shape[1], num_classes=3)
model_pol, history_pol = train_model(model_pol, train_pol, val_pol, device=device)"""),

        code("""plot_training_curves(history_pol, 'MLP TF-IDF — Polarité')

preds_pol, labels_pol = evaluate_model(model_pol, test_pol, device=device)
print_report(labels_pol, preds_pol, POLARITY_NAMES, 'MLP TF-IDF — Polarité (Test)')
plot_confusion(labels_pol, preds_pol, POLARITY_NAMES, 'MLP TF-IDF — Polarité')"""),

        md("## 5. Score (1-5 étoiles)"),

        code("""train_sc, val_sc, test_sc = make_loaders(
    X_train, y_sc_train, X_val, y_sc_val, X_test, y_sc_test
)

model_score = MLP(X_train.shape[1], num_classes=5)
model_score, history_score = train_model(model_score, train_sc, val_sc, device=device)"""),

        code("""plot_training_curves(history_score, 'MLP TF-IDF — Score')

preds_sc, labels_sc = evaluate_model(model_score, test_sc, device=device)
# Reconvertir en 1-5 pour l'affichage
print_report(labels_sc, preds_sc, SCORE_NAMES, 'MLP TF-IDF — Score (Test)')
plot_confusion(labels_sc, preds_sc, SCORE_NAMES, 'MLP TF-IDF — Score')"""),

        md("## 6. Sauvegarde"),

        code("""from sklearn.metrics import f1_score, accuracy_score

comparison = pd.DataFrame({
    'Tâche': ['Polarité', 'Score'],
    'Accuracy': [accuracy_score(labels_pol, preds_pol), accuracy_score(labels_sc, preds_sc)],
    'F1 Macro': [f1_score(labels_pol, preds_pol, average='macro'),
                 f1_score(labels_sc, preds_sc, average='macro')],
})
print("=== RÉSUMÉ MLP TF-IDF ===")
display(comparison)

torch.save(model_pol.state_dict(), os.path.join(MODELS_DIR, 'mlp_tfidf_polarity.pt'))
torch.save(model_score.state_dict(), os.path.join(MODELS_DIR, 'mlp_tfidf_score.pt'))
print(f"\\nModèles sauvegardés dans {MODELS_DIR}")"""),
    ]


# ============================================================
# 02-deep-ngram.ipynb — CNN 1D sur N-Grammes
# ============================================================
def gen_02():
    return [
        md("""# Deep Learning sur N-Grammes — CNN 1D

CNN 1D PyTorch sur features N-grammes pour la classification de sentiment Yelp.

**Architecture** : Conv1d(k=3,4,5) parallèle → MaxPool → Dense → Output

**Deux tâches** : Polarité (3 classes) et Score (1-5 étoiles)"""),

        code("""import sys
sys.path.insert(0, '../..')

import os
import pandas as pd
import torch
import torch.nn as nn
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import warnings
warnings.filterwarnings('ignore')

from src.constants import POLARITY_NAMES, SCORE_NAMES
from src.ml_utils import load_and_prepare, split_data
from src.dl_utils import get_device, set_seed, make_loaders, train_model, evaluate_model
from src.evaluation import plot_confusion, plot_training_curves, print_report
from src import setup_plot_style

setup_plot_style()
set_seed()
device = get_device()
MODELS_DIR = '../../models/'
os.makedirs(MODELS_DIR, exist_ok=True)
print(f'Device : {device}')"""),

        md("## 1. Chargement et Préparation"),

        code("""df = load_and_prepare()
data = split_data(df['text'], df['polarity'], df['stars'])
print(f"Train: {len(data['X_train'])} | Val: {len(data['X_val'])} | Test: {len(data['X_test'])}")"""),

        md("## 2. Vectorisation N-Grammes"),

        code("""VOCAB_SIZE = 10_000

vectorizer = CountVectorizer(max_features=VOCAB_SIZE, min_df=5, max_df=0.7, ngram_range=(1, 2))

X_train = vectorizer.fit_transform(data['X_train']).toarray()
X_val = vectorizer.transform(data['X_val']).toarray()
X_test = vectorizer.transform(data['X_test']).toarray()

# Score 0-indexed pour PyTorch
y_sc_train = (data['y_sc_train'] - 1).values.astype(int)
y_sc_val = (data['y_sc_val'] - 1).values.astype(int)
y_sc_test = (data['y_sc_test'] - 1).values.astype(int)

print(f'Matrice N-grammes : {X_train.shape}')"""),

        md("""## 3. Architecture CNN 1D

Convolutions parallèles (Kim 2014) avec kernels 3, 4, 5 suivies de max-pooling global."""),

        code("""class TextCNN1D(nn.Module):
    def __init__(self, vocab_size, num_classes=5, num_filters=128,
                 kernel_sizes=(3, 4, 5), dropout=0.5):
        super().__init__()
        self.convs = nn.ModuleList([
            nn.Conv1d(1, num_filters, k) for k in kernel_sizes
        ])
        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(num_filters * len(kernel_sizes), 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = x.unsqueeze(1)  # (batch, vocab) → (batch, 1, vocab)
        pooled = [self.relu(conv(x)).max(dim=2).values for conv in self.convs]
        out = torch.cat(pooled, dim=1)
        out = self.dropout(out)
        out = self.relu(self.fc1(out))
        out = self.dropout(out)
        return self.fc2(out)

model_test = TextCNN1D(VOCAB_SIZE, 3)
print(model_test)
print(f'\\nParamètres : {sum(p.numel() for p in model_test.parameters() if p.requires_grad):,}')
del model_test"""),

        md("## 4. Polarité (3 classes)"),

        code("""train_pol, val_pol, test_pol = make_loaders(
    X_train, data['y_pol_train'].values,
    X_val, data['y_pol_val'].values,
    X_test, data['y_pol_test'].values,
    batch_size=64
)

model_pol = TextCNN1D(VOCAB_SIZE, num_classes=3)
model_pol, history_pol = train_model(
    model_pol, train_pol, val_pol, device=device, epochs=15, patience=3
)"""),

        code("""plot_training_curves(history_pol, 'CNN 1D N-Grammes — Polarité')

preds_pol, labels_pol = evaluate_model(model_pol, test_pol, device=device)
print_report(labels_pol, preds_pol, POLARITY_NAMES, 'CNN 1D — Polarité (Test)')
plot_confusion(labels_pol, preds_pol, POLARITY_NAMES, 'CNN 1D — Polarité')"""),

        md("## 5. Score (1-5 étoiles)"),

        code("""train_sc, val_sc, test_sc = make_loaders(
    X_train, y_sc_train, X_val, y_sc_val, X_test, y_sc_test, batch_size=64
)

model_score = TextCNN1D(VOCAB_SIZE, num_classes=5)
model_score, history_score = train_model(
    model_score, train_sc, val_sc, device=device, epochs=15, patience=3
)"""),

        code("""plot_training_curves(history_score, 'CNN 1D N-Grammes — Score')

preds_sc, labels_sc = evaluate_model(model_score, test_sc, device=device)
print_report(labels_sc, preds_sc, SCORE_NAMES, 'CNN 1D — Score (Test)')
plot_confusion(labels_sc, preds_sc, SCORE_NAMES, 'CNN 1D — Score')"""),

        md("## 6. Sauvegarde"),

        code("""from sklearn.metrics import f1_score, accuracy_score

comparison = pd.DataFrame({
    'Tâche': ['Polarité', 'Score'],
    'Accuracy': [accuracy_score(labels_pol, preds_pol), accuracy_score(labels_sc, preds_sc)],
    'F1 Macro': [f1_score(labels_pol, preds_pol, average='macro'),
                 f1_score(labels_sc, preds_sc, average='macro')],
})
print("=== RÉSUMÉ CNN 1D N-GRAMMES ===")
display(comparison)

torch.save(model_pol.state_dict(), os.path.join(MODELS_DIR, 'cnn1d_ngram_polarity.pt'))
torch.save(model_score.state_dict(), os.path.join(MODELS_DIR, 'cnn1d_ngram_score.pt'))
joblib.dump(vectorizer, os.path.join(MODELS_DIR, 'count_vectorizer_deep.pkl'))
print(f"\\nModèles sauvegardés dans {MODELS_DIR}")"""),
    ]


# ============================================================
# 03-deep-llm.ipynb — Fine-tuning DistilBERT
# ============================================================
def gen_03():
    return [
        md("""# Fine-tuning DistilBERT (Deep-LLM)

Fine-tuning de **DistilBERT** pré-entraîné pour la classification de sentiment Yelp.

**Architecture** : DistilBERT → [CLS] → Dropout → Dense(768→256) → ReLU → Dense(256→N)

**Deux tâches** : Polarité (3 classes) et Score (1-5 étoiles)

**Corrections vs version précédente :**
- Fix NameError dans la cellule de sauvegarde
- Suppression des cellules papermill erreur"""),

        code("""import sys
sys.path.insert(0, '../..')

import os
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from transformers import DistilBertTokenizer, DistilBertModel
import warnings
warnings.filterwarnings('ignore')

from src.constants import RANDOM_STATE, POLARITY_NAMES, SCORE_NAMES
from src.ml_utils import load_and_prepare, split_data
from src.dl_utils import get_device, set_seed
from src.evaluation import plot_confusion, plot_training_curves, print_report
from src import setup_plot_style

setup_plot_style()
set_seed()
device = get_device()
MODELS_DIR = '../../models/'
os.makedirs(MODELS_DIR, exist_ok=True)
print(f'Device : {device}')"""),

        md("## 1. Chargement des Données"),

        code("""df = load_and_prepare(sample_size=5000)
data = split_data(df['text'], df['polarity'], df['stars'])

X_train = data['X_train'].tolist()
X_val = data['X_val'].tolist()
X_test = data['X_test'].tolist()

# Score 0-indexed pour PyTorch
y_pol_train = data['y_pol_train'].values
y_pol_val = data['y_pol_val'].values
y_pol_test = data['y_pol_test'].values
y_sc_train = (data['y_sc_train'] - 1).values.astype(int)
y_sc_val = (data['y_sc_val'] - 1).values.astype(int)
y_sc_test = (data['y_sc_test'] - 1).values.astype(int)

print(f'Train : {len(X_train)} | Val : {len(X_val)} | Test : {len(X_test)}')"""),

        md("## 2. Tokenisation DistilBERT"),

        code("""MODEL_NAME = 'distilbert-base-uncased'
MAX_LENGTH = 128
BATCH_SIZE = 16

tokenizer = DistilBertTokenizer.from_pretrained(MODEL_NAME)
print(f'Tokenizer {MODEL_NAME} chargé.')


class YelpDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.encodings = tokenizer(
            texts, truncation=True, padding='max_length',
            max_length=max_length, return_tensors='pt'
        )
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {k: v[idx] for k, v in self.encodings.items()}
        item['labels'] = self.labels[idx]
        return item


def make_bert_loaders(y_train, y_val, y_test):
    return (
        DataLoader(YelpDataset(X_train, y_train, tokenizer, MAX_LENGTH),
                    batch_size=BATCH_SIZE, shuffle=True),
        DataLoader(YelpDataset(X_val, y_val, tokenizer, MAX_LENGTH),
                    batch_size=BATCH_SIZE),
        DataLoader(YelpDataset(X_test, y_test, tokenizer, MAX_LENGTH),
                    batch_size=BATCH_SIZE),
    )"""),

        md("## 3. Modèle DistilBERT + Classification"),

        code("""class DistilBertClassifier(nn.Module):
    def __init__(self, model_name, num_classes=5, dropout=0.3):
        super().__init__()
        self.bert = DistilBertModel.from_pretrained(model_name)
        hidden = self.bert.config.hidden_size
        self.classifier = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(hidden, 256), nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(256, num_classes)
        )

    def forward(self, input_ids, attention_mask):
        out = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        cls = out.last_hidden_state[:, 0, :]
        return self.classifier(cls)"""),

        md("## 4. Fonctions d'entraînement"),

        code("""def train_bert(model, train_loader, val_loader, epochs=5, lr=2e-5, patience=2):
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=0.01)

    history = {'train_loss': [], 'val_loss': [], 'train_acc': [], 'val_acc': []}
    best_val_loss = float('inf')
    best_state = None
    patience_counter = 0

    for epoch in range(epochs):
        # Train
        model.train()
        t_loss, t_correct, t_total = 0, 0, 0
        for batch in train_loader:
            ids = batch['input_ids'].to(device)
            mask = batch['attention_mask'].to(device)
            y = batch['labels'].to(device)
            optimizer.zero_grad()
            logits = model(ids, mask)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()
            t_loss += loss.item() * len(y)
            t_correct += (logits.argmax(1) == y).sum().item()
            t_total += len(y)

        # Val
        model.eval()
        v_loss, v_correct, v_total = 0, 0, 0
        with torch.no_grad():
            for batch in val_loader:
                ids = batch['input_ids'].to(device)
                mask = batch['attention_mask'].to(device)
                y = batch['labels'].to(device)
                logits = model(ids, mask)
                loss = criterion(logits, y)
                v_loss += loss.item() * len(y)
                v_correct += (logits.argmax(1) == y).sum().item()
                v_total += len(y)

        tl, vl = t_loss/t_total, v_loss/v_total
        ta, va = t_correct/t_total, v_correct/v_total
        history['train_loss'].append(tl)
        history['val_loss'].append(vl)
        history['train_acc'].append(ta)
        history['val_acc'].append(va)

        print(f'Epoch {epoch+1}/{epochs} | Train loss: {tl:.4f} acc: {ta:.4f} | Val loss: {vl:.4f} acc: {va:.4f}')

        if vl < best_val_loss:
            best_val_loss = vl
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print(f"Early stopping à l'epoch {epoch+1}")
                break

    model.load_state_dict(best_state)
    return model, history


def eval_bert(model, loader):
    model.eval()
    preds, labels = [], []
    with torch.no_grad():
        for batch in loader:
            ids = batch['input_ids'].to(device)
            mask = batch['attention_mask'].to(device)
            logits = model(ids, mask)
            preds.extend(logits.argmax(1).cpu().numpy())
            labels.extend(batch['labels'].numpy())
    return np.array(preds), np.array(labels)"""),

        md("## 5. Polarité (3 classes)"),

        code("""train_pol, val_pol, test_pol = make_bert_loaders(y_pol_train, y_pol_val, y_pol_test)

model_pol = DistilBertClassifier(MODEL_NAME, num_classes=3)
model_pol, history_pol = train_bert(model_pol, train_pol, val_pol)"""),

        code("""plot_training_curves(history_pol, 'DistilBERT — Polarité')

preds_pol, labels_pol = eval_bert(model_pol, test_pol)
print_report(labels_pol, preds_pol, POLARITY_NAMES, 'DistilBERT — Polarité (Test)')
plot_confusion(labels_pol, preds_pol, POLARITY_NAMES, 'DistilBERT — Polarité')"""),

        md("## 6. Score (1-5 étoiles)"),

        code("""train_sc, val_sc, test_sc = make_bert_loaders(y_sc_train, y_sc_val, y_sc_test)

model_score = DistilBertClassifier(MODEL_NAME, num_classes=5)
model_score, history_score = train_bert(model_score, train_sc, val_sc)"""),

        code("""plot_training_curves(history_score, 'DistilBERT — Score')

preds_sc, labels_sc = eval_bert(model_score, test_sc)
print_report(labels_sc, preds_sc, SCORE_NAMES, 'DistilBERT — Score (Test)')
plot_confusion(labels_sc, preds_sc, SCORE_NAMES, 'DistilBERT — Score')"""),

        md("## 7. Sauvegarde"),

        code("""from sklearn.metrics import f1_score, accuracy_score

acc_pol = accuracy_score(labels_pol, preds_pol)
f1_pol = f1_score(labels_pol, preds_pol, average='macro')
acc_sc = accuracy_score(labels_sc, preds_sc)
f1_sc = f1_score(labels_sc, preds_sc, average='macro')

comparison = pd.DataFrame({
    'Tâche': ['Polarité', 'Score'],
    'Accuracy': [acc_pol, acc_sc],
    'F1 Macro': [f1_pol, f1_sc],
})
print("=== RÉSUMÉ DISTILBERT FINE-TUNING ===")
display(comparison)

# Sauvegarder les modèles
final_dir = os.path.join(MODELS_DIR, 'distilbert_finetuned')
os.makedirs(final_dir, exist_ok=True)

torch.save({
    'model_state_dict': model_pol.state_dict(),
    'model_name': MODEL_NAME, 'num_classes': 3, 'max_length': MAX_LENGTH,
    'accuracy_test': acc_pol, 'f1_macro_test': f1_pol, 'task': 'polarity'
}, os.path.join(final_dir, 'model_polarity.pt'))

torch.save({
    'model_state_dict': model_score.state_dict(),
    'model_name': MODEL_NAME, 'num_classes': 5, 'max_length': MAX_LENGTH,
    'accuracy_test': acc_sc, 'f1_macro_test': f1_sc, 'task': 'score'
}, os.path.join(final_dir, 'model_score.pt'))

tokenizer.save_pretrained(os.path.join(final_dir, 'tokenizer'))
print(f'\\nModèles sauvegardés dans {final_dir}/')"""),
    ]


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    base = 'notebooks/5-deep-learning'
    print('Génération des notebooks DL refactorisés...')
    save_nb(gen_01(), f'{base}/01-deep-tfidf.ipynb')
    save_nb(gen_02(), f'{base}/02-deep-ngram.ipynb')
    save_nb(gen_03(), f'{base}/03-deep-llm.ipynb')
    # 04-ia-generative.ipynb est géré par des édits minimaux (notebook unique)
    print('Done!')
