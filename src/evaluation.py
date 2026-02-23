"""
Fonctions d'évaluation partagées pour ML et Deep Learning.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix
)


def compute_metrics(y_true, y_pred, average='macro'):
    """Calcule les métriques de classification."""
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average=average, zero_division=0),
        'recall': recall_score(y_true, y_pred, average=average, zero_division=0),
        'f1': f1_score(y_true, y_pred, average=average, zero_division=0),
    }


def evaluate_classifier(model, X_train, y_train, X_eval, y_eval, average='macro'):
    """Évalue un modèle sklearn sur train et eval, retourne métriques + prédictions."""
    y_pred_train = model.predict(X_train)
    y_pred_eval = model.predict(X_eval)

    metrics = compute_metrics(y_eval, y_pred_eval, average=average)
    metrics['train_acc'] = accuracy_score(y_train, y_pred_train)
    metrics['overfit_gap'] = metrics['train_acc'] - metrics['accuracy']

    return metrics, y_pred_eval


def plot_confusion(y_true, y_pred, labels, title, save_path=None):
    """Affiche la matrice de confusion."""
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=labels, yticklabels=labels)
    plt.title(f'Matrice de confusion — {title}')
    plt.ylabel('Vrai')
    plt.xlabel('Prédit')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_training_curves(history, title, save_path=None):
    """Affiche les courbes loss et accuracy d'entraînement DL."""
    epochs = range(1, len(history['train_loss']) + 1)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    ax1.plot(epochs, history['train_loss'], label='Train', marker='o', markersize=4)
    ax1.plot(epochs, history['val_loss'], label='Val', marker='s', markersize=4)
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.set_title(f'{title} — Loss')
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.plot(epochs, history['train_acc'], label='Train', marker='o', markersize=4)
    ax2.plot(epochs, history['val_acc'], label='Val', marker='s', markersize=4)
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Accuracy')
    ax2.set_title(f'{title} — Accuracy')
    ax2.legend()
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def print_report(y_true, y_pred, target_names, title):
    """Affiche un rapport complet de classification."""
    metrics = compute_metrics(y_true, y_pred)
    print(f'\n=== {title} ===')
    print(f'Accuracy  : {metrics["accuracy"]:.4f}')
    print(f'F1 Macro  : {metrics["f1"]:.4f}')
    print(f'Precision : {metrics["precision"]:.4f}')
    print(f'Recall    : {metrics["recall"]:.4f}')
    print(classification_report(y_true, y_pred, target_names=target_names, zero_division=0))
    return metrics
