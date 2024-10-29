import re
from collections import Counter

from typing import List, Dict

def search_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Функция для поиска транзакций по описанию с использованием регулярных выражений."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction['description'])]


def count_categories(transactions: List[Dict]) -> Dict[str, int]:
    """Функция для подсчёта количества операций по категориям."""
    categories = [transaction['description'] for transaction in transactions]
    return dict(Counter(categories))
