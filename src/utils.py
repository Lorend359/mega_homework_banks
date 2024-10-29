import json
import logging
import os
from typing import Any, Dict, List

from src.external_api import convert_to_rub

# Настройка логирования
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler(os.path.join(log_dir, "utils.log"), mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка формата логов
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    """
    logger.info(f"Загрузка транзакций из {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    if os.path.getsize(file_path) == 0:
        logger.warning(f"Файл пуст: {file_path}")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            logger.info(f"Транзакции успешно загружены: {data}")
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []


def get_transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях."""
    try:
        amount = float(transaction.get("operationAmount", {}).get("amount", 0))
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

        if currency in ["USD", "EUR"]:
            return convert_to_rub(amount, currency)

        if currency is None or currency not in ["RUB", "USD", "EUR"]:
            raise ValueError("Unsupported currency")

        logger.info(f"Сумма транзакции: {amount} в валюте {currency}")
        return amount

    except ValueError as e:
        logger.error(f"Ошибка при получении суммы транзакции: {e}")
        raise


if __name__ == "__main__":
    # Попытка загрузки из несуществующего файла
    non_existent_transactions = load_transactions("неправильный_путь.json")

    # Проверка, была ли ошибка при загрузке
    if non_existent_transactions is None:
        logger.error("Не удалось загрузить транзакции: файл не найден или недоступен.")

    # Попытка загрузки из существующего файла
    valid_transactions = load_transactions("../data/operations.json")

    if valid_transactions:
        print("Транзакции успешно загружены.")

        # Некорректные данные транзакции
        invalid_transaction = {"operationAmount": {"amount": "нечисловое значение", "currency": {"code": "USD"}}}
        try:
            print(get_transaction_amount(invalid_transaction))
        except ValueError as e:
            logger.exception(f"Ошибка при получении суммы транзакции: {e}")
    else:
        logger.error("Не удалось загрузить транзакции: пустой результат загрузки.")
