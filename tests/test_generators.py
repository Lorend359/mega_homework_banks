from src.generators import filter_by_currency

import pytest


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2020-05-05T10:15:25.123456",
            "operationAmount": {
                "amount": "5000.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Обмен валюты",
            "from": "Счет 98765432109876543210",
            "to": "Счет 12345678901234567890"
        }
    ]

@pytest.mark.parametrize("currency_code, expected", [
    ('USD', [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]),
    ('EUR', [
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2020-05-05T10:15:25.123456",
            "operationAmount": {
                "amount": "5000.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Обмен валюты",
            "from": "Счет 98765432109876543210",
            "to": "Счет 12345678901234567890"
        }
    ]),
    ('JPY', []),
])
def test_filter_by_currency(transactions, currency_code, expected):
    result = list(filter_by_currency(transactions, currency_code))
    assert result == expected

def test_empty_transactions():
    result = list(filter_by_currency([], 'USD'))
    assert result == []

