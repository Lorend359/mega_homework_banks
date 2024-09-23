from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """
    Функция проверяет счёт или номер карты на входе,
    и маскирует соответствующее с использованием функций из masks.py
    """

    last_space_index = card_info.rfind(' ')
    if last_space_index == -1:
        raise ValueError("Неверный формат входной строки.")

    card_type = card_info[:last_space_index]
    number = card_info[last_space_index + 1:]

    number = "".join(filter(str.isdigit, number))

    if len(number) in range(16, 20):
        return get_mask_card_number(card_type, number)
    elif len(number) >= 10:
        return get_mask_account(card_type, number)
    else:
        raise ValueError("Неизвестный тип номера.")


def get_date(date_string: str) -> str:
    """Функция, которая изменяет на классический формат даты"""

    date_part = date_string.split("T")[0]

    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"