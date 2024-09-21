from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """
    Функция проверяет счёт или номер карты на неё подан
    И маскирует соответствующе реализации функций в masks.py
    """
    number = "".join(filter(str.isdigit, card_number))

    if len(number) >= 16 and len(number) <= 19:  # Примерное ограничение для карт
        return get_mask_card_number(number)
    elif len(number) >= 10:  # Предположим, что номер счёта не меньше 10 цифр
        return get_mask_account(number)
    else:
        raise ValueError("Неизвестный тип номера.")


def get_date(given_date: str) -> str:
    """Функция которая классический формат даты"""
    pass
