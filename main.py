from src.csv_xlsx_reader import read_csv_transactions, read_excel_transactions
from src.decorators import log
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transaction_processing import search_transactions
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


@log()
def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()
    transactions = []

    if choice == "1":
        transactions = load_transactions("src/files/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        transactions = read_csv_transactions("src/files/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        transactions = read_excel_transactions("src/files/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Недопустимый выбор.")
        return

    VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию."
                " Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
            )
            .strip()
            .upper()
        )
        if status in VALID_STATUSES:
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен. Попробуйте еще раз.')

    filtered_transactions = list(filter_by_state(transactions, status))

    if filtered_transactions:
        while True:
            sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
            if sort_choice not in {"да", "нет"}:
                print("Пожалуйста, введите 'Да' или 'Нет'.")
            else:
                if sort_choice == "да":
                    while True:
                        order = (
                            input("Сортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ")
                            .strip()
                            .lower()
                        )
                        if order in {"по возрастанию", "по убыванию"}:
                            filtered_transactions = list(
                                sort_by_date(filtered_transactions, sort=(order != "по убыванию"))
                            )
                            break
                        else:
                            print("Пожалуйста, введите 'по возрастанию' или 'по убыванию'.")
                break

        currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
        if currency_filter == "да":
            filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))

        search_choice = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
        )
        if search_choice == "да":
            search_string = input("Введите слово для поиска: ").strip()
            filtered_transactions = list(search_transactions(filtered_transactions, search_string))

        print("Распечатываю итоговый список транзакций...")

        if filtered_transactions:
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
            for transaction in filtered_transactions:
                date_str = transaction.get("date")
                formatted_date = get_date(date_str) if date_str is not None else "Дата недоступна"
                description = transaction.get("description")

                amount = (
                    transaction["operationAmount"].get("amount")
                    if "operationAmount" in transaction
                    else transaction.get("amount")
                )
                currency_name = (
                    transaction["operationAmount"]["currency"].get("name")
                    if "operationAmount" in transaction
                    else transaction.get("currency_name")
                )


                from_ = str(transaction.get("from")) if transaction.get("from") is not None else None
                to = str(transaction.get("to")) if transaction.get("to") is not None else None

                print(f"{formatted_date} {description}")


                masked_from = mask_account_card(from_) if from_ else "→ Не указано"
                masked_to = mask_account_card(to) if to else "→ Не указано"

                print(f"{masked_from} → {masked_to}")
                print(f"Сумма: {amount} {currency_name}\n")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()


# from src.masks import get_mask_card_number, get_mask_account
# from src.processing import result_filter_by_state, result_sort_by_date
# from src.widget import get_date, mask_account_card


# print(get_mask_card_number((input())))
# print(get_mask_account((input())))
# print(mask_account_card(input()))
# print(get_date("2024-03-11T02:26:18.671407"))
# print(result_filter_by_state)
# print(result_sort_by_date)
