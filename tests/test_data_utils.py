"""
Tests unitaires pour src/data_utils.py
"""

import pytest
import pandas as pd
from pathlib import Path
from src.data_utils import load_parquet


class TestLoadParquet:
    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            load_parquet("nonexistent.parquet", base_path="/tmp")

    def test_loads_dataframe(self, tmp_path):
        # Créer un parquet temporaire
        df = pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"]})
        filepath = tmp_path / "test.parquet"
        df.to_parquet(filepath)

        result = load_parquet("test.parquet", base_path=str(tmp_path))
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 3

    def test_column_selection(self, tmp_path):
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
        filepath = tmp_path / "test.parquet"
        df.to_parquet(filepath)

        result = load_parquet("test.parquet", base_path=str(tmp_path), columns=["a"])
        assert list(result.columns) == ["a"]
