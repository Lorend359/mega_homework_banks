import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

""" Тесты filter_by_currency"""


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2020-05-05T10:15:25.123456",
            "operationAmount": {"amount": "5000.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Обмен валюты",
            "from": "Счет 98765432109876543210",
            "to": "Счет 12345678901234567890",
        },
    ]


@pytest.mark.parametrize(
    "currency_code, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        (
            "EUR",
            [
                {
                    "id": 123456789,
                    "state": "EXECUTED",
                    "date": "2020-05-05T10:15:25.123456",
                    "operationAmount": {"amount": "5000.00", "currency": {"name": "EUR", "code": "EUR"}},
                    "description": "Обмен валюты",
                    "from": "Счет 98765432109876543210",
                    "to": "Счет 12345678901234567890",
                }
            ],
        ),
        ("JPY", []),
    ],
)
def test_filter_by_currency(transactions, currency_code, expected):
    result = list(filter_by_currency(transactions, currency_code))
    assert result == expected


def test_empty_transactions():
    result = list(filter_by_currency([], "USD"))
    assert result == []


""" Тесты transaction_descriptions"""


@pytest.fixture
def transactions_data():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 999999999,
            "state": "EXECUTED",
            "date": "2020-01-01T00:00:00.000000",
            "operationAmount": {"amount": "1000.00", "currency": {"name": "руб.", "code": "RUB"}},
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321",
        },
    ]


@pytest.mark.parametrize(
    "expected, index",
    [
        ("Перевод организации", 0),
        ("Перевод со счета на счет", 1),
        ("Перевод со счета на счет", 2),
        ("Перевод с карты на карту", 3),
        ("Перевод организации", 4),
        ("Нет описания", 5),
    ],
)
def test_transaction_descriptions(transactions_data, expected, index):
    transactions = transactions_data
    generator = transaction_descriptions(transactions)
    for i, description in enumerate(generator):
        if i == index:
            assert description == expected


"""Тесты для card_number_generator"""


@pytest.fixture
def test_data():
    return [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            10,
            12,
            [
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
            ],
        ),
        (
            0,
            0,
            [
                "0000 0000 0000 0000",
            ],
        ),
    ]


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            10,
            12,
            [
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
            ],
        ),
        (
            0,
            0,
            [
                "0000 0000 0000 0000",
            ],
        ),
    ],
)
def test_card_number_generator(start, end, expected):
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected


def test_card_number_generator_empty():
    generated_numbers = list(card_number_generator(1, 0))
    assert generated_numbers == []
