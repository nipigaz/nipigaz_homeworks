# src/external_api.py
import os
import requests
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert'


def convert_to_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными транзакции
    :return: Сумма в рублях (float)
    """
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    if currency not in ('USD', 'EUR'):
        raise ValueError('Unsupported currency')

    response = requests.get(
        BASE_URL,
        params={
            'from': currency,
            'to': 'RUB',
            'amount': amount
        },
        headers={'apikey': API_KEY}
    )
    response.raise_for_status()
    return response.json()['result']
