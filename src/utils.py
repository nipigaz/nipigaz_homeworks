# src/utils.py
import json
from typing import List, Dict


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает данные о транзакциях из JSON-файла.

    :param file_path: Путь к JSON-файлу
    :return: Список словарей с транзакциями или пустой список при ошибках
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    