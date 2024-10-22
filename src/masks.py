import logging
import os

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(log_dir, 'masks.log'), mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_type: str, card_number: str) -> str:
    """Маскирует номер банковской карты."""
    if not card_number:
        logger.warning(f"Получен пустой номер карты для типа {card_type}.")
        return f"{card_type} None** **** None"

    if len(card_number) < 16:
        logger.info(f"Краткий номер карты для типа {card_type}: {card_number}.")
        return f"{card_type} {card_number} ** **** {card_number[-4:]}"

    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Замаскированный номер карты для типа {card_type}: {masked_card}.")
    return f"{card_type} {masked_card}"


def get_mask_account(account_type: str, account_number: str) -> str:
    """Маскирует номер банковского счёта"""
    if not account_number.isdigit():
        logger.error(f"{account_type} содержит недопустимые символы: {account_number}.")
        raise ValueError(f"{account_type} содержит недопустимые символы")

    masked_account = f"**{account_number[-4:]}"
    logger.info(f"Замаскированный номер счёта для типа {account_type}: {masked_account}.")
    return f"{account_type} {masked_account}"

#Вызов для проверки правильных данных
get_mask_card_number("Visa", "1234567812345678")
get_mask_account("Bank Account", "123456789012345")

#Вызов ошибки
try:
    get_mask_account("Bank Account", "not_a_number")  # Ошибка
except ValueError:
    pass
