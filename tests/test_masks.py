import pytest
from src.masks import get_mask_card_number, get_mask_account
from typing import List, Tuple, Union


# Фикстуры для общих тестовых данных
@pytest.fixture
def valid_card_numbers() -> List[Tuple[Union[str, int], str]]:
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        (7000792289606361, "7000 79** **** 6361"),
        ("4111111111111111", "4111 11** **** 1111")
    ]


@pytest.fixture
def invalid_card_numbers() -> List[Tuple[str, str]]:
    return [
        ("123456789012345", "15 символов"),
        ("12345678901234567", "17 символов"),
        ("", "Пустая строка"),
        ("abcd567890123456", "Буквы в номере")
    ]


@pytest.fixture
def valid_accounts() -> List[Tuple[Union[str, int], str]]:
    return [
        ("73654108430135874305", "**4305"),
        (987654, "**7654"),
        ("1234", "**1234")
    ]


# Тесты для get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    pytest.param("7000792289606361", "7000 79** **** 6361", id="стандартная строка"),
    pytest.param(7000792289606361, "7000 79** **** 6361", id="числовой ввод"),
    pytest.param("4111111111111111", "4111 11** **** 1111", id="другой номер"),
])
def test_valid_card_masking(card_number: Union[str, int], expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_input, error_msg", [
    ("123456789012345", "Номер карты должен быть 16 символов."),
    ("abcd567890123456", "Номер карты должен состоять только из цифр."),
    (12345, "Номер карты должен быть 16 символов."),
], ids=["короткий номер", "нечисловые символы", "число короткое"])
def test_card_exceptions(invalid_input: Union[str, int], error_msg: str) -> None:
    with pytest.raises(ValueError, match=error_msg):
        get_mask_card_number(invalid_input)


# Тесты для get_mask_account
@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    (987654321, "**4321"),
    ("0000", "**0000")
], ids=["длинный счет", "числовой ввод", "нулевые значения"])
def test_valid_account_masking(account_number: Union[str, int], expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("invalid_input, error_msg", [
    ("123", "Номер счета должен иметь минимум 4 цифры."),
    (45, "Номер счета должен иметь минимум 4 цифры."),
    ("", "Номер счета должен иметь минимум 4 цифры.")
], ids=["3 символа", "2 цифры", "пустая строка"])
def test_account_exceptions(invalid_input: Union[str, int], error_msg: str) -> None:
    with pytest.raises(ValueError, match=error_msg):
        get_mask_account(invalid_input)
