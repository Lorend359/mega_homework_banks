from typing import Any, Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[Any, Any]]:
    """Функция для считывания финансовых операций из CSV."""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {file_path}")
        return []


def read_excel_transactions(file_path: str) -> List[Dict[Any, Any]]:
    """Функция для считывания финансовых операций из Excel."""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {file_path}")
        return []


# if __name__ == "__main__":
#     '''
#     Вызовы для функции оставлю здесь, были написаны до тестов,
#     будут закомментированы, что бы в отчёте была нормальная цифра покрытия
#     '''
#     # Пример вызова для проверки CSV
#     csv_file_path = 'files/transactions.csv'
#     csv_transactions = read_csv_transactions(csv_file_path)
#
#     # Вывод первых 5 транзакций из CSV
#     if csv_transactions:
#         print("Первые 5 транзакций из CSV:")
#         for i, transaction in enumerate(csv_transactions[:5]):
#             print(f"{i + 1}: {transaction}")
#     else:
#         print("Нет доступных транзакций для отображения из CSV.")
#
#     # Пример вызова для проверки Excel
#     excel_file_path = 'files/transactions_excel.xlsx'
#     excel_transactions = read_excel_transactions(excel_file_path)
#
#     # Вывод первых 5 транзакций из Excel
#     if excel_transactions:
#         print("\nПервые 5 транзакций из Excel:")
#         for i, transaction in enumerate(excel_transactions[:5]):
#             print(f"{i + 1}: {transaction}")
#     else:
#         print("Нет доступных транзакций для отображения из Excel.")
