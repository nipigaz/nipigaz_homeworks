import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
        Считывает финансовые операции из CSV файла.

        Параметры:
        file_path (str): Путь к CSV файлу.

        Возвращает:
        List[Dict]: Список словарей с транзакциями.
        """
    try:
        df = pd.read_csv(file_path, delimiter=';')
        # Проверяем наличие ожидаемых колонок
        expected_columns = ['date', 'amount', 'description']
        if not all(col in df.columns for col in expected_columns):
            print("Ошибка: CSV файл содержит неверные колонки")
            return []
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel файла.

    Параметры:
    file_path (str): Путь к Excel файлу.

    Возвращает:
    List[Dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel файла: {e}")
        return []
