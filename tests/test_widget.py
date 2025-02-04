import pytest
from src.widget import mask_account_card, get_date
# from typing import Any


# Тесты для функции mask_account_card
@pytest.mark.parametrize("input_data, expected", [
    pytest.param("Visa Platinum 7000792289606361", "Visa 7000 79** **** 6361", id="Visa Platinum"),
    pytest.param("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456", id="MasterCard"),
    pytest.param("Maestro 9876543210987654", "Maestro 9876 54** **** 7654", id="Maestro"),
])
def test_mask_account_card_cards(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize("input_data, expected", [
    pytest.param("Счет 73654108430135874305", "Счет **4305", id="Длинный счет"),
    pytest.param("Счет 1234567890123456", "Счет **3456", id="Короткий счет"),
])
def test_mask_account_card_accounts(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize("invalid_input", [
    "Счет 123",  # Номер счета слишком короткий
    "Visa 123456789012345",  # Номер карты слишком короткий
    "Invalid Input",  # Некорректный ввод
])
def test_mask_account_card_invalid_input(invalid_input: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(invalid_input)


# Тесты для функции get_date
@pytest.mark.parametrize("input_data, expected", [
    pytest.param("2024-03-11T02:26:18.671407", "11.03.2024", id="Корректная дата 1"),
    pytest.param("2023-12-31T23:59:59.999999", "31.12.2023", id="Корректная дата 2"),
    pytest.param("2022-01-01T00:00:00.000000", "01.01.2022", id="Корректная дата 3"),
])
def test_get_date_valid(input_data: str, expected: str) -> None:
    assert get_date(input_data) == expected


@pytest.mark.parametrize("invalid_input", [
    "2024-03-11",  # Отсутствует часть времени
    "2024/03/11T02:26:18.671407",  # Неправильный разделитель
    "Invalid Date",  # Некорректный ввод
])
def test_get_date_invalid_input(invalid_input: str) -> None:
    with pytest.raises(ValueError):
        get_date(invalid_input)
