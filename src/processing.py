def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по значению ключа 'state'.
    :параметр operations: Список словарей с данными о банковских операциях.
    :параметр state: Значение для фильтрации по ключу 'state'. По умолчанию 'EXECUTED'.
    :return: Отфильтрованный список словарей.
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список операций по дате.

    :параметр operations: Список словарей с данными о банковских операциях.
    :параметр reverse: Если True, сортировка по убыванию (по умолчанию). Если False, по возрастанию.
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

# Фильтрация по состоянию
filtered_data = filter_by_state(data_state, state="EXECUTED")
print("Отфильтрованные данные:")
print(filtered_data)

# Сортировка по дате
sorted_data = sort_by_date(data_date, reverse=True)
print("Отсортированные данные:")
print(sorted_data)
