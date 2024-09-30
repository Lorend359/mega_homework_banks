import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def card_data():
    return [
        ("Visa Platinum", "7000792289606361"),
        ("Maestro", "1596837868705199"),
        ("MasterCard", "7158300734726758"),
        ("Visa Classic", "6831982476737658"),
        ("Visa Platinum", "8990922113665229"),
        ("Visa Gold", "5999414228426353"),
    ]

@pytest.mark.parametrize("card_type, card_number, expected", [
    ("Visa Platinum", "7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro", "1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard", "7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic", "6831982476736758", "Visa Classic 6831 98** **** 6758"),
    ("Visa Platinum", "8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold", "5999414228426353", "Visa Gold 5999 41** **** 6353"),
])
def test_get_mask_card_number(card_type, card_number, expected):
    assert get_mask_card_number(card_type, card_number) == expected

def test_get_mask_card_number_empty():
    assert get_mask_card_number("Visa", "") == "Visa None** **** None"

def test_get_mask_card_number_short():
    assert get_mask_card_number("Test Card", "1234") == "Test Card 1234 ** **** 1234"


@pytest.fixture
def account_data():
    return [
        ("Счет", "73654108430135874305"),
        ("Счет", "1234567890123456"),
        ("Счет", "987654321"),
        ("Счет", "1"),
        ("Счет", ""),
    ]

# Параметризованные тесты
@pytest.mark.parametrize("account_type, account_number, expected", [
    ("Счет", "73654108430135874305", "Счет **4305"),
    ("Счет", "1234567890123456", "Счет **3456"),
    ("Счет", "987654321", "Счет **4321"),
    ("Счет", "1", "Счет **1"),  # даже если номер меньше 4 цифр
])
def test_get_mask_account(account_type, account_number, expected):
    assert get_mask_account(account_type, account_number) == expected

# Тест для проверки неправильного ввода
def test_get_mask_account_invalid_input():
    with pytest.raises(ValueError, match="Счет содержит недопустимые символы"):
        get_mask_account("Счет", "abc")

    with pytest.raises(ValueError, match="Счет содержит недопустимые символы"):
        get_mask_account("Счет", "123abc")

    with pytest.raises(ValueError, match="Счет содержит недопустимые символы"):
        get_mask_account("Счет", "!@#$")

    with pytest.raises(ValueError, match="Счет содержит недопустимые символы"):
        get_mask_account("Счет", "")
