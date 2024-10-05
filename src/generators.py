def filter_by_currency(transactions, currency_code):
    """Функция, которая принимает на вход список словарей, представляющих транзакции."""
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction

