def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(card_number: str) -> str:
    """Маскирует номер банковского счёта"""
    return f"**{card_number[-4:]}"
