import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions

class TestLoadTransactions:

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}]')
    @patch("os.path.exists", return_value=True)
    def test_valid_file(self, _, __):
        result = load_transactions("data/operations.json")
        assert result == [{"id": 1}]

    @patch("builtins.open", new_callable=mock_open, read_data='')
    @patch("os.path.exists", return_value=True)
    def test_empty_file(self, _, __):
        result = load_transactions("data/operations.json")
        assert result == []

    @patch("builtins.open", new_callable=mock_open, read_data='not a json')
    @patch("os.path.exists", return_value=True)
    def test_invalid_json(self, _, __):
        result = load_transactions("data/operations.json")
        assert result == []

    @patch("os.path.exists", return_value=False)
    def test_file_not_found(self, _):
        result = load_transactions("data/operations.json")
        assert result == []