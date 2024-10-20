import json
import os
from typing import Any, Dict, List

from src.external_api import convert_to_rub


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    """
    if not os.path.exists(file_path):
        return []

    if os.path.getsize(file_path) == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []


def get_transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях."""

    amount = transaction.get("amount", 0)
    currency = transaction.get("currency")

    if currency in ["USD", "EUR"]:
        return convert_to_rub(amount, currency)

    if currency is None or currency not in ["RUB", "USD", "EUR"]:
        raise ValueError("Unsupported currency")

    return float(amount)
