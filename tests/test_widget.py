import pytest
from src.widget import mask_account_card


@pytest.fixture
def card_data():
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **8560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 6758"),
    ]

@pytest.fixture
def incorrect_data():
    return [
        "" ,
        "Некорректный текст",
        "Счет 12345",
        "SomeBank 123456",
    ]

@pytest.mark.parametrize("input_data, expected_output", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447898560", "Счет **8560"),
    ("Visa Classic 6831982476736758", "Visa Classic 6831 98** **** 6758")
])
def test_mask_account_card(card_data, input_data, expected_output):
    assert mask_account_card(input_data) == expected_output

@pytest.mark.parametrize("input_data", [
    "",
    "Некорректный текст",
    "Счет 12345",
    "SomeBank 123456"
])
def test_mask_account_card_incorrect(incorrect_data, input_data):
    assert mask_account_card(input_data) is None