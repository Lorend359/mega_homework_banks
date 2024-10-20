import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions


@patch("os.path.exists")
def test_load_transactions_file_not_found(mock_exists):
    mock_exists.return_value = False
    result = load_transactions("non_existing_file.json")
    assert result == []


@patch("os.path.exists")
@patch("os.path.getsize")
def test_load_transactions_empty_file(mock_getsize, mock_exists):
    mock_exists.return_value = True
    mock_getsize.return_value = 0
    result = load_transactions("empty_file.json")
    assert result == []


@patch("os.path.exists")
@patch("os.path.getsize")
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"key": "value"}))
def test_load_transactions_not_a_list(mock_open_func, mock_getsize, mock_exists):
    mock_exists.return_value = True
    mock_getsize.return_value = len(mock_open_func().read())
    result = load_transactions("not_a_list.json")
    assert result == []


@patch("os.path.exists")
@patch("os.path.getsize")
@patch(
    "builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
)
def test_load_transactions_valid_list(mock_open_func, mock_getsize, mock_exists):
    mock_exists.return_value = True
    mock_getsize.return_value = len(mock_open_func().read())
    result = load_transactions("valid_file.json")
    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


@patch("os.path.exists")
@patch("os.path.getsize")
@patch("builtins.open", new_callable=mock_open, read_data="{invalid json}")
def test_load_transactions_invalid_json(mock_open_func, mock_getsize, mock_exists):
    mock_exists.return_value = True
    mock_getsize.return_value = len(mock_open_func().read())
    result = load_transactions("invalid_json.json")
    assert result == []
