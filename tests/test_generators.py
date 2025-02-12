import pytest
from typing import List

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions() -> list[dict]:
    """Фикстура с примером транзакций для тестирования."""
    return [
        {
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 895315941,
            "operationAmount": {"amount": "56883.54", "currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]


def test_filter_by_currency(sample_transactions: List[dict]) -> None:
    """
    Проверка фильтрации транзакций по валюте USD.

    Тест проверяет:
    - Корректное извлечение трех транзакций с кодом "USD".
    - Завершение генератора (StopIteration) после последней транзакции.
    """
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_filter_by_currency_no_matches(sample_transactions: list[dict]) -> None:
    """
    Проверка обработки отсутствия подходящих транзакций.

    Тест проверяет, что генератор не возвращает транзакции для несуществующей валюты "EUR".
    """
    eur_transactions = filter_by_currency(sample_transactions, "EUR")
    with pytest.raises(StopIteration):
        next(eur_transactions)


def test_filter_by_currency_empty() -> None:
    """
    Проверка обработки пустого списка транзакций.

    Тест проверяет, что генератор завершается сразу при отсутствии входных данных.
    """
    empty_transactions = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(empty_transactions)


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    """
    Проверка извлечения описаний транзакций.

    Тест проверяет:
    - Корректность порядка описаний.
    - Соответствие текста описаний.
    - Завершение генератора после обработки всех транзакций.
    """
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_empty() -> None:
    """
    Проверка обработки пустого списка транзакций.

    Тест проверяет, что генератор завершается сразу при отсутствии входных данных.
    """
    empty_descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(empty_descriptions)


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: list[str]) -> None:
    """
    Параметризованный тест генератора номеров карт.

    Проверяет:
    - Корректность генерации номеров в различных диапазонах.
    - Правильность форматирования (XXXX XXXX XXXX XXXX).

    :param start: Начало диапазона
    :param end: Конец диапазона
    :param expected: Ожидаемые номера карт
    """
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected


def test_card_number_generator_invalid_range() -> None:
    """
    Проверка обработки некорректного диапазона (start > end).

    Тест проверяет, что генератор не возвращает значений при start > end.
    """

    generated_numbers = list(card_number_generator(5, 1))
    assert generated_numbers == []
