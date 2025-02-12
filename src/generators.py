from typing import Dict, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> [Dict]:
    """
    Генератор, фильтрующий транзакции по заданному коду валюты.

    :параметр transactions: Список транзакций (словарей)
    :параметр currency_code: Код валюты для фильтрации (например, "USD")
    :yield: Транзакции, соответствующие заданной валюте
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> [str]:
    """
    Генератор, возвращающий описание транзакций.

    :параметр transactions: Список транзакций (словарей)
    :yield: Описание каждой транзакции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> [str]:
    """
    Генератор номеров банковских карт в заданном диапазоне.

    :param start: Начальное значение диапазона (включительно)
    :param end: Конечное значение диапазона (включительно)
    :yield: Номер карты в формате "XXXX XXXX XXXX XXXX"
    """
    for num in range(start, end + 1):
        num_str = str(num).zfill(16)
        formatted_number = " ".join([num_str[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_number
