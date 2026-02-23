"""
Utilitaires ML pour le projet S6C01.

Fonctions partagées : chargement données, split, grilles d'hyperparamètres, tuning.
"""

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB

from .constants import RANDOM_STATE, SAMPLE_SIZE, stars_to_polarity
from .data_utils import load_parquet
from .evaluation import evaluate_classifier


def load_and_prepare(sample_size=SAMPLE_SIZE, base_path='../../data/cleaned',
                     columns=None):
    """Charge les reviews, ajoute la colonne polarity, échantillonne."""
    cols = columns or ['text', 'stars']
    df = load_parquet('reviews_clean.parquet', base_path=base_path, columns=cols)
    df = df.dropna(subset=['text', 'stars'])
    df['polarity'] = df['stars'].apply(stars_to_polarity)

    if sample_size and sample_size < len(df):
        df = df.sample(n=sample_size, random_state=RANDOM_STATE)

    return df


def split_data(X, y_polarity, y_score):
    """Split 80/10/10 stratifié sur la polarité. Retourne un dict."""
    X_train, X_temp, y_pol_train, y_pol_temp, y_sc_train, y_sc_temp = train_test_split(
        X, y_polarity, y_score,
        test_size=0.20, random_state=RANDOM_STATE, stratify=y_polarity
    )
    X_val, X_test, y_pol_val, y_pol_test, y_sc_val, y_sc_test = train_test_split(
        X_temp, y_pol_temp, y_sc_temp,
        test_size=0.50, random_state=RANDOM_STATE, stratify=y_pol_temp
    )
    return {
        'X_train': X_train, 'X_val': X_val, 'X_test': X_test,
        'y_pol_train': y_pol_train, 'y_pol_val': y_pol_val, 'y_pol_test': y_pol_test,
        'y_sc_train': y_sc_train, 'y_sc_val': y_sc_val, 'y_sc_test': y_sc_test,
    }


def get_param_grids(use_gaussian_nb=False):
    """Retourne les grilles d'hyperparamètres pour les 4 algorithmes ML.

    Grilles optimisées empiriquement (voir scripts/optimize_models.py) :
    - use_gaussian_nb=False → TF-IDF/N-grammes (sparse) : saga, C plus élevé
    - use_gaussian_nb=True  → Embeddings LLM (dense)   : lbfgs, C plus bas
    """
    if use_gaussian_nb:
        # Embeddings denses → lbfgs (rapide), C bas, var_smoothing pour NB
        solver, penalty = ['lbfgs'], ['l2']
        c_values = [0.001, 0.01, 0.1, 1, 10]
        nb_class = GaussianNB()
        nb_params = {'var_smoothing': [1e-11, 1e-10, 1e-9, 1e-8, 1e-7]}
    else:
        # TF-IDF sparse → saga (supporte L1), C plus élevé
        solver, penalty = ['saga'], ['l1', 'l2']
        c_values = [0.01, 0.1, 1, 10, 50]
        nb_class = MultinomialNB()
        nb_params = {'alpha': [0.01, 0.1, 0.5, 1.0, 2.0]}

    return {
        'Logistic Regression': {
            'model': LogisticRegression(
                max_iter=1000, random_state=RANDOM_STATE, n_jobs=-1,
                class_weight='balanced'
            ),
            'params': {
                'C': c_values,
                'penalty': penalty,
                'solver': solver,
            }
        },
        'Linear SVC': {
            'model': LinearSVC(
                random_state=RANDOM_STATE, max_iter=2000, dual='auto',
                class_weight='balanced'
            ),
            'params': {
                'C': c_values,
            }
        },
        'Random Forest': {
            'model': RandomForestClassifier(
                random_state=RANDOM_STATE, n_jobs=-1,
                class_weight='balanced'
            ),
            'params': {
                'n_estimators': [100, 200],
                'max_depth': [10, 30, None],
                'min_samples_leaf': [1, 5],
            }
        },
        'Naive Bayes': {
            'model': nb_class,
            'params': nb_params,
        },
    }


def tune_and_evaluate(param_grids, X_train, y_train, X_val, y_val):
    """Tune chaque modèle avec GridSearchCV puis évalue sur val."""
    results = {}
    best_models = {}
    predictions = {}

    for name, config in param_grids.items():
        print(f'\n--- {name} (GridSearchCV 5-fold) ---')
        gs = GridSearchCV(
            config['model'], config['params'],
            cv=5, scoring='f1_macro', n_jobs=-1, refit=True
        )
        gs.fit(X_train, y_train)

        best_model = gs.best_estimator_
        best_models[name] = best_model

        metrics, y_pred = evaluate_classifier(
            best_model, X_train, y_train, X_val, y_val
        )
        results[name] = metrics
        predictions[name] = y_pred

        print(f'  Meilleurs params : {gs.best_params_}')
        print(f'  CV F1 Macro      : {gs.best_score_:.4f}')
        print(f'  Train Acc : {metrics["train_acc"]:.4f} | Val Acc : {metrics["accuracy"]:.4f} | '
              f'Val F1 : {metrics["f1"]:.4f} | Overfit Gap : {metrics["overfit_gap"]:+.4f}')

    return results, best_models, predictions
