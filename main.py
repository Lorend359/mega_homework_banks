
import json
import csv
import pandas as pd  # Для XLSX
from src.transaction_processing import search_transactions, count_categories
from typing import List, Dict
import os

def load_transactions_from_json(file_path: str) -> List[Dict]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_transactions_from_csv(file_path: str) -> List[Dict]:
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_transactions_from_xlsx(file_path: str) -> List[Dict]:
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    transactions = []

    # Определяем путь к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Получаем абсолютный путь к текущей директории
    csv_file_path = os.path.join(current_dir, 'files', 'transactions.csv')
    xlsx_file_path = os.path.join(current_dir, 'files', 'transactions_excel.xlsx')

    if choice == '1':
        file_path = input("Введите путь к JSON файлу: ")
        transactions = load_transactions_from_json(file_path)
    elif choice == '2':
        if not os.path.exists(csv_file_path):
            print(f"Файл {csv_file_path} не найден.")
            return
        transactions = load_transactions_from_csv(csv_file_path)
    elif choice == '3':
        if not os.path.exists(xlsx_file_path):
            print(f"Файл {xlsx_file_path} не найден.")
            return
        transactions = load_transactions_from_xlsx(xlsx_file_path)
    else:
        print("Недопустимый выбор.")
        return

    status = input("Введите статус, по которому необходимо выполнить фильтрацию. "
                   "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n")

    filtered_transactions = search_transactions(transactions, status)

    print("Распечатываю итоговый список транзакций...")

    for transaction in filtered_transactions:
        print(transaction)

    # Подсчет категорий
    category_counts = count_categories(filtered_transactions)
    print("\nКоличество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

if __name__ == "__main__":
    main()










#from src.masks import get_mask_card_number, get_mask_account
#from src.processing import result_filter_by_state, result_sort_by_date
#from src.widget import get_date, mask_account_card


#print(get_mask_card_number((input())))
#print(get_mask_account((input())))
#print(mask_account_card(input()))
#print(get_date("2024-03-11T02:26:18.671407"))
# print(result_filter_by_state)
# print(result_sort_by_date)