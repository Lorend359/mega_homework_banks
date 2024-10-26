
from unittest.mock import patch
import pandas as pd
from src.csv_xlsx_reader import read_csv_transactions, read_excel_transactions

@patch('pandas.read_csv')
def test_read_csv_transactions_success(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({
        'id': [1, 2],
        'amount': [100.0, 200.0],
        'currency': ['USD', 'EUR']
    })

    expected_result = [
        {'id': 1, 'amount': 100.0, 'currency': 'USD'},
        {'id': 2, 'amount': 200.0, 'currency': 'EUR'}
    ]

    result = read_csv_transactions('dummy_path')
    assert result == expected_result

@patch('pandas.read_csv')
def test_read_csv_transactions_file_not_found(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError

    result = read_csv_transactions('dummy_path')
    assert result == []

@patch('pandas.read_excel')
def test_read_excel_transactions_success(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame({
        'id': [1, 2],
        'amount': [150.0, 250.0],
        'currency': ['USD', 'EUR']
    })

    expected_result = [
        {'id': 1, 'amount': 150.0, 'currency': 'USD'},
        {'id': 2, 'amount': 250.0, 'currency': 'EUR'}
    ]

    result = read_excel_transactions('dummy_path')
    assert result == expected_result

@patch('pandas.read_excel')
def test_read_excel_transactions_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError

    result = read_excel_transactions('dummy_path')
    assert result == []
