import pytest
import pandas as pd
from tempfile import NamedTemporaryFile
import os
from src.financial_operation_reader import read_transactions_from_csv, read_transactions_from_excel

# Тесты для read_transactions_from_csv


def test_read_transactions_from_csv_success():
    # Создаем временный CSV файл с корректными данными
    csv_data = "date;amount;description\n2023-01-01;100;Payment\n2023-01-02;200;Transfer"
    with NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        f.write(csv_data)
        file_path = f.name

    # Вызываем функцию и проверяем результат
    result = read_transactions_from_csv(file_path)
    assert len(result) == 2
    assert result[0] == {"date": "2023-01-01", "amount": 100, "description": "Payment"}
    os.unlink(file_path)  # Удаляем временный файл


def test_read_transactions_from_csv_file_not_found():
    result = read_transactions_from_csv("non_existent.csv")
    assert result == []


def test_read_transactions_from_csv_invalid_format():
    # Создаем CSV с разделителем ',', что приводит к неверным колонкам
    csv_data = "date,amount,description\n2023-01-01,100,Payment"
    with NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        f.write(csv_data)
        file_path = f.name

    result = read_transactions_from_csv(file_path)
    assert result == []  # Теперь функция вернет пустой список из-за несоответствия колонок
    os.unlink(file_path)


# Тесты для read_transactions_from_excel
def test_read_transactions_from_excel_success():
    # Создаем временный Excel файл
    df = pd.DataFrame([
        {"date": "2023-01-01", "amount": 100, "description": "Payment"},
        {"date": "2023-01-02", "amount": 200, "description": "Transfer"}
    ])
    with NamedTemporaryFile(delete=False, suffix='.xlsx') as f:
        df.to_excel(f.name, index=False, engine='openpyxl')
        file_path = f.name

    result = read_transactions_from_excel(file_path)
    assert len(result) == 2
    assert result[0]["amount"] == 100
    os.unlink(file_path)


def test_read_transactions_from_excel_file_not_found():
    result = read_transactions_from_excel("non_existent.xlsx")
    assert result == []


def test_read_transactions_from_excel_invalid_engine():
    # Создаем битый файл или файл с неподдерживаемым форматом
    with NamedTemporaryFile(delete=False, suffix='.xlsx') as f:
        # Записываем некорректные данные
        f.write(b"Invalid content")
        file_path = f.name

    result = read_transactions_from_excel(file_path)
    assert result == []
    os.unlink(file_path)
