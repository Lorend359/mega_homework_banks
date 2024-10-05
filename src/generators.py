def filter_by_currency(transactions, currency_code):
    """Функция, которая принимает на вход список словарей, представляющих транзакции."""
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции по очереди.
    """
    for transaction in transactions:
        yield transaction.get('description', 'Нет описания')


def card_number_generator(start, end):
    ''' Генератор номеров банковских карт'''
    pass