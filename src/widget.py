from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """
    Функция проверяет счёт или номер карты на неё подан
    И маскирует соответствующе реализации функций в masks.py
    """
    number = "".join(filter(str.isdigit, card_number))

    if len(number) in range(16, 20):
        return get_mask_card_number(number)
    elif len(number) >= 10:
        return get_mask_account(number)
    else:
        raise ValueError("Неизвестный тип номера.")


def get_date(date_string: str) -> str:
    """Функция, которая изменяет на классический формат даты"""

    date_part = date_string.split("T")[0]

    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
