def filter_by_currency(transactions, currency_code):
    """Функция, которая принимает на вход список словарей, представляющих транзакции."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции по очереди.
    """
    for transaction in transactions:
        yield transaction.get("description", "Нет описания")


def card_number_generator(start, end):
    """Генератор номеров банковских карт"""
    for number in range(start, end + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        yield card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:16]
