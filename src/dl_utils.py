"""
Utilitaires Deep Learning (PyTorch) pour le projet S6C01.
"""

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

from .constants import RANDOM_STATE


def get_device():
    """Sélectionne le meilleur device disponible (MPS > CUDA > CPU)."""
    if torch.backends.mps.is_available():
        return torch.device('mps')
    elif torch.cuda.is_available():
        return torch.device('cuda')
    return torch.device('cpu')


def set_seed(seed=RANDOM_STATE):
    """Fixe les graines aléatoires pour la reproductibilité."""
    torch.manual_seed(seed)
    np.random.seed(seed)


def make_loaders(X_train, y_train, X_val, y_val, X_test, y_test, batch_size=256):
    """Convertit les arrays numpy en DataLoaders PyTorch."""
    def _to_ds(X, y):
        return TensorDataset(
            torch.tensor(X, dtype=torch.float32),
            torch.tensor(y, dtype=torch.long)
        )
    return (
        DataLoader(_to_ds(X_train, y_train), batch_size=batch_size, shuffle=True),
        DataLoader(_to_ds(X_val, y_val), batch_size=batch_size),
        DataLoader(_to_ds(X_test, y_test), batch_size=batch_size),
    )


def train_model(model, train_loader, val_loader, device=None,
                epochs=50, lr=1e-3, patience=5):
    """Entraîne un modèle PyTorch avec early stopping. Retourne model + history."""
    if device is None:
        device = get_device()
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    history = {'train_loss': [], 'val_loss': [], 'train_acc': [], 'val_acc': []}
    best_val_loss = float('inf')
    best_state = None
    patience_counter = 0

    for epoch in range(epochs):
        # --- Train ---
        model.train()
        t_loss, t_correct, t_total = 0, 0, 0
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
            t_loss += loss.item() * X_batch.size(0)
            t_correct += (outputs.argmax(1) == y_batch).sum().item()
            t_total += X_batch.size(0)

        # --- Val ---
        model.eval()
        v_loss, v_correct, v_total = 0, 0, 0
        with torch.no_grad():
            for X_batch, y_batch in val_loader:
                X_batch, y_batch = X_batch.to(device), y_batch.to(device)
                outputs = model(X_batch)
                loss = criterion(outputs, y_batch)
                v_loss += loss.item() * X_batch.size(0)
                v_correct += (outputs.argmax(1) == y_batch).sum().item()
                v_total += X_batch.size(0)

        tl = t_loss / t_total
        vl = v_loss / v_total
        ta = t_correct / t_total
        va = v_correct / v_total
        history['train_loss'].append(tl)
        history['val_loss'].append(vl)
        history['train_acc'].append(ta)
        history['val_acc'].append(va)

        if vl < best_val_loss:
            best_val_loss = vl
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1

        if (epoch + 1) % 5 == 0 or patience_counter >= patience:
            print(f'Epoch {epoch+1:3d}/{epochs} | '
                  f'Train Loss: {tl:.4f} Acc: {ta:.4f} | '
                  f'Val Loss: {vl:.4f} Acc: {va:.4f}')

        if patience_counter >= patience:
            print(f"Early stopping à l'epoch {epoch+1}")
            break

    model.load_state_dict(best_state)
    return model, history


def evaluate_model(model, test_loader, device=None):
    """Évalue un modèle PyTorch, retourne (preds, labels) en numpy."""
    if device is None:
        device = get_device()
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            X_batch = X_batch.to(device)
            preds = model(X_batch).argmax(1).cpu().numpy()
            all_preds.extend(preds)
            all_labels.extend(y_batch.numpy())
    return np.array(all_preds), np.array(all_labels)
