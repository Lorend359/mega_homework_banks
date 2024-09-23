def get_mask_card_number(card_type: str, card_number: str) -> str:
    """Маскирует номер банковской карты"""
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_type} {masked_card}"


def get_mask_account(account_type: str, account_number: str) -> str:
    """Маскирует номер банковского счёта"""
    masked_account = f"**{account_number[-4:]}"
    return f"{account_type} {masked_account}"
