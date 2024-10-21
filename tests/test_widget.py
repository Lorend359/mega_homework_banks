import pytest

from src.widget import get_date, mask_account_card


# Тесты для данных карт и счёта
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
        "",
        "Некорректный текст",
        "Счет 12345",
        "SomeBank 123456",
    ]


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447898560", "Счет **8560"),
        ("Visa Classic 6831982476736758", "Visa Classic 6831 98** **** 6758"),
    ],
)
def test_mask_account_card(card_data, input_data, expected_output):
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize("input_data", ["", "Некорректный текст", "Счет 12345", "SomeBank 123456"])
def test_mask_account_card_incorrect(incorrect_data, input_data):
    assert mask_account_card(input_data) is None


# Тесты для даты
@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2021-01-01T00:00:00", "01.01.2021"),
        ("1999-12-31T23:59:59", "31.12.1999"),
        ("2000-02-29T12:45:30", "29.02.2000"),  # Год високосный
    ],
)
def test_get_date_valid(input_date, expected_output):
    assert get_date(input_date) == expected_output


@pytest.mark.parametrize(
    "input_date",
    [
        "",
        "Некорректный текст",
        "2024/03/11T02:26:18",
        "2024-03-11",
    ],
)
def test_get_date_invalid(input_date):
    with pytest.raises(ValueError):
        get_date(input_date)
