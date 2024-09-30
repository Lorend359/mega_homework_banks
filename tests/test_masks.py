import pytest

from src.masks import get_mask_account, get_mask_card_number

@pytest.fixture
def card_data():
    return [
        ("Visa", "1234567812345678", "Visa 1234 56** **** 5678"),
        ("MasterCard", "8765432187654321", "MasterCard 8765 43** **** 4321"),
        ("American Express", "378282246310005", "American Express 3782 82** **** 0005"),
    ]


@pytest.mark.parametrize("card_type, card_number, expected_output", [
    ("Visa", "1234567812345678", "Visa 1234 56** **** 5678"),
    ("MasterCard", "8765432187654321", "MasterCard 8765 43** **** 4321"),
    ("American Express", "378282246310005", "American Express 3782 82** **** 0005"),
])
def test_get_mask_card_number(card_data, card_type, card_number, expected_output):
    result = get_mask_card_number(card_type, card_number)
    assert result == expected_output