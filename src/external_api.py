import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """Конвертация суммы в рубли с использованием внешнего API."""

    if currency not in ["USD", "EUR"]:
        raise ValueError("Unsupported currency")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"

    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Error fetching data from the API")

    data = response.json()
    exchange_rate = data["rates"]["RUB"]

    return amount * exchange_rate
