import pytest
from src.transaction_processing import search_transactions, count_categories

def test_search_transactions_no_matches():
    transactions = [
        {'description': 'Открытие вклада'},
        {'description': 'Перевод организации'},
    ]
    result = search_transactions(transactions, 'не существующая строка')
    assert len(result) == 0

def test_count_categories_empty():
    transactions = []
    result = count_categories(transactions)
    assert result == {}

def test_count_categories_multiple_types():
    transactions = [
        {'description': 'Открытие вклада'},
        {'description': 'Перевод организации'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Открытие вклада'},
        {'description': 'Перевод с карты на карту'},
    ]
    result = count_categories(transactions)
    assert result['Открытие вклада'] == 2
    assert result['Перевод с карты на карту'] == 2
    assert result['Перевод организации'] == 1

def test_count_categories_with_unexpected_description():
    transactions = [
        {'description': 'Неизвестная операция'},
        {'description': 'Перевод организации'},
    ]
    result = count_categories(transactions)
    assert result['Неизвестная операция'] == 1
    assert result['Перевод организации'] == 1