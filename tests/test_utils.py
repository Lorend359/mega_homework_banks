import json
from unittest.mock import mock_open, patch

import pytest

from src.external_api import convert_to_rub
from src.utils import get_transaction_amount, load_transactions

""" Тесты для load_transactions"""


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


"""Тесты для get_transaction_amount"""


def test_get_transaction_amount_rub():
    transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
    result = get_transaction_amount(transaction)
    assert result == 1000.0


@patch("src.utils.convert_to_rub")
def test_get_transaction_amount_usd(mock_convert):
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    mock_convert.return_value = 7000.0
    result = get_transaction_amount(transaction)
    assert result == 7000.0
    mock_convert.assert_called_once_with(100.0, "USD")


@patch("src.utils.convert_to_rub")
def test_get_transaction_amount_eur(mock_convert):
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}  #
    mock_convert.return_value = 8500.0
    result = get_transaction_amount(transaction)
    assert result == 8500.0
    mock_convert.assert_called_once_with(100.0, "EUR")


def test_get_transaction_amount_unsupported_currency():
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "GBP"}}}
    with pytest.raises(ValueError, match="Unsupported currency"):
        get_transaction_amount(transaction)


def test_get_transaction_amount_missing_currency():
    transaction = {"operationAmount": {"amount": "100"}}
    with pytest.raises(ValueError, match="Unsupported currency"):
        get_transaction_amount(transaction)


""" Тесты для конвертации рубля"""


@patch("requests.get")
def test_convert_to_rub_success(mock_get):
    mock_response = {"rates": {"RUB": 70.0}}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    amount = 100
    currency = "USD"
    result = convert_to_rub(amount, currency)
    assert result == 7000.0


@patch("requests.get")
def test_convert_to_rub_unsupported_currency(mock_get):
    with pytest.raises(ValueError, match="Unsupported currency"):
        convert_to_rub(100, "GBP")


@patch("requests.get")
def test_convert_to_rub_api_failure(mock_get):
    mock_get.return_value.status_code = 500
    with pytest.raises(Exception, match="Error fetching data from the API"):
        convert_to_rub(100, "USD")


@patch("requests.get")
def test_convert_to_rub_invalid_rate(mock_get):
    mock_response = {"rates": {"RUB": "invalid"}}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    with pytest.raises(ValueError, match="Exchange rate is not a number"):
        convert_to_rub(100, "USD")
