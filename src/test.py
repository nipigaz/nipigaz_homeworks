from typing import List, Dict


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по значению ключа 'state'.
    :param operations: Список словарей с данными о банковских операциях.
    :param state: Значение для фильтрации по ключу 'state' ("EXECUTED" или "CANCELED"). По умолчанию "EXECUTED".
    :return: Отфильтрованный список словарей.
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.
    :param operations: Список словарей с данными о банковских операциях.
    :param reverse: Если True, сортировка по убыванию (по умолчанию). Если False — по возрастанию.
    :return: Отсортированный список словарей.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)


# Примеры входных данных
data_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2019-01-22T10:15:00.511233"},
]

data_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# Примеры использования
if __name__ == "__main__":
    # Фильтрация по "EXECUTED" (используется data_state)
    executed_operations = filter_by_state(data_state, state="EXECUTED")
    print("Отфильтрованные операции (EXECUTED):")
    print(executed_operations)

    # Фильтрация по "CANCELED" (используется data_state)
    canceled_operations = filter_by_state(data_state, state="CANCELED")
    print("Отфильтрованные операции (CANCELED):")
    print(canceled_operations)

    # Сортировка по убыванию (используется data_date)
    sorted_desc = sort_by_date(data_date, reverse=True)
    print("\nОтсортированные операции (по убыванию):")
    print(sorted_desc)

    # Сортировка по возрастанию (используется data_date)
    sorted_asc = sort_by_date(data_date, reverse=False)
    print("\nОтсортированные операции (по возрастанию):")
    print(sorted_asc)