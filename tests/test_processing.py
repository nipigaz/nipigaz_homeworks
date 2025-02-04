import pytest
from src.processing import filter_by_state, sort_by_date
# from datetime import datetime


# Фикстуры для тестовых данных
@pytest.fixture
def operations_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 123456789, "state": "PENDING", "date": "2020-01-01T00:00:00.000000"},
    ]


@pytest.fixture
def operations_without_state():
    return [
        {"id": 1, "date": "2021-01-01T00:00:00.000000"},
        {"id": 2, "date": "2021-02-01T00:00:00.000000"},
    ]


@pytest.fixture
def operations_with_invalid_dates():
    return [
        {"id": 1, "state": "EXECUTED", "date": "invalid-date"},
        {"id": 2, "state": "EXECUTED", "date": "2021-01-01T00:00:00.000000"},
    ]


# Тесты для функции filter_by_state
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("PENDING", 1),
    ("UNKNOWN", 0),
])
def test_filter_by_state(operations_data, state, expected_count):
    filtered_operations = filter_by_state(operations_data, state)
    assert len(filtered_operations) == expected_count
    for operation in filtered_operations:
        assert operation["state"] == state


def test_filter_by_state_without_state_key(operations_without_state):
    filtered_operations = filter_by_state(operations_without_state, "EXECUTED")
    assert len(filtered_operations) == 0


# Тесты для функции sort_by_date
@pytest.mark.parametrize("reverse, expected_first_id", [
    (True, 123456789),  # Сортировка по убыванию (самая поздняя дата)
    (False, 939719570),  # Сортировка по возрастанию (самая ранняя дата)
])
def test_sort_by_date(operations_data, reverse, expected_first_id):
    sorted_operations = sort_by_date(operations_data, reverse)
    assert sorted_operations[0]["id"] == expected_first_id


def test_sort_by_date_with_invalid_dates(operations_with_invalid_dates):
    with pytest.raises(ValueError):
        sort_by_date(operations_with_invalid_dates)


def test_sort_by_date_with_identical_dates():
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01T00:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "date": "2021-01-01T00:00:00.000000"},
    ]
    sorted_operations = sort_by_date(operations, reverse=True)
    assert sorted_operations[0]["id"] in [1, 2]
    assert sorted_operations[1]["id"] in [1, 2]
