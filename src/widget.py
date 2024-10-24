from typing import Any

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> Any:
    """
    Функция проверяет счёт или номер карты на входе,
    и маскирует соответствующее с использованием функций из masks.py
    """

    last_space_index = card_info.rfind(" ")

    card_type = card_info[:last_space_index]
    number = card_info[last_space_index + 1 :]

    number = "".join(filter(str.isdigit, number))

    if len(number) in range(16, 20):
        return get_mask_card_number(card_type, number)
    elif len(number) >= 10:
        return get_mask_account(card_type, number)


def get_date(date_string: str) -> str:
    """Функция, которая изменяет на классический формат даты"""

    if not date_string:
        raise ValueError("Input date string cannot be empty.")

    if "T" not in date_string or len(date_string.split("T")) != 2:
        raise ValueError("Invalid date format. Expected format: YYYY-MM-DDTHH:MM:SS")

    date_part = date_string.split("T")[0]

    try:
        year, month, day = date_part.split("-")
    except ValueError:
        raise ValueError("Invalid date format. Expected format: YYYY-MM-DD")

    return f"{day}.{month}.{year}"
