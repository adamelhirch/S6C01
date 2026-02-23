"""
Test smoke du pipeline d'inférence.
Vérifie que le pipeline sauvegardé peut charger et prédire.
"""

import os
import pytest
import numpy as np
import joblib

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPELINE_DIR = os.path.join(ROOT_DIR, "models", "pipeline_optimal")


@pytest.fixture(scope="module")
def pipeline_models():
    """Charge les modèles du pipeline sauvegardé."""
    polarity_path = os.path.join(PIPELINE_DIR, "logreg_polarity.pkl")
    score_path = os.path.join(PIPELINE_DIR, "logreg_score.pkl")
    metadata_path = os.path.join(PIPELINE_DIR, "metadata.pkl")

    if not all(os.path.exists(p) for p in [polarity_path, score_path, metadata_path]):
        pytest.skip("Modèles pipeline non trouvés (fichiers .pkl gitignorés)")

    return {
        "polarity": joblib.load(polarity_path),
        "score": joblib.load(score_path),
        "metadata": joblib.load(metadata_path),
    }


class TestPipelineMetadata:
    def test_metadata_keys(self, pipeline_models):
        meta = pipeline_models["metadata"]
        assert "model_name" in meta
        assert "embedding_dim" in meta
        assert meta["embedding_dim"] == 768

    def test_metadata_scores(self, pipeline_models):
        meta = pipeline_models["metadata"]
        assert meta["polarity_f1"] > 0.5
        assert meta["score_f1"] > 0.3


class TestPipelinePrediction:
    def test_polarity_predict(self, pipeline_models):
        model = pipeline_models["polarity"]
        # Embedding factice de dimension 768
        fake_embedding = np.random.randn(1, 768)
        pred = model.predict(fake_embedding)
        assert pred[0] in [0, 1, 2]

    def test_polarity_proba(self, pipeline_models):
        model = pipeline_models["polarity"]
        fake_embedding = np.random.randn(1, 768)
        proba = model.predict_proba(fake_embedding)
        assert proba.shape == (1, 3)
        assert abs(proba.sum() - 1.0) < 1e-6

    def test_score_predict(self, pipeline_models):
        model = pipeline_models["score"]
        fake_embedding = np.random.randn(1, 768)
        pred = model.predict(fake_embedding)
        assert pred[0] in [1, 2, 3, 4, 5]

    def test_score_proba(self, pipeline_models):
        model = pipeline_models["score"]
        fake_embedding = np.random.randn(1, 768)
        proba = model.predict_proba(fake_embedding)
        assert proba.shape == (1, 5)
        assert abs(proba.sum() - 1.0) < 1e-6

    def test_batch_prediction(self, pipeline_models):
        model = pipeline_models["polarity"]
        batch = np.random.randn(10, 768)
        preds = model.predict(batch)
        assert len(preds) == 10
        assert all(p in [0, 1, 2] for p in preds)
