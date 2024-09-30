import pytest
from src.masks import get_mask_card_number

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