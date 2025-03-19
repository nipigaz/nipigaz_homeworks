import logging
import json
from typing import List, Dict

# Настройка логирования для модуля utils
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Формат записи логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

# Вызов логирования
logger.info('Запуск программы.')
logger.debug('Это сообщение для отладки.')
logger.error('Тестовое сообщение об ошибке.')

# После завершения работы приложения
file_handler.close()
logger.removeHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает данные о транзакциях из JSON-файла.

    :параметр file_path: Путь к JSON-файлу
    :return: Список словарей с транзакциями или пустой список при ошибках
    """
    logger.debug("Загрузка транзакций из файла: %s", file_path)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Успешная загрузка транзакций.")
                return data
            else:
                logger.warning("Данные не являются списком.")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден: %s", file_path)
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON в файле: %s", file_path)

    logger.debug("Возвращаем пустой список.")
    return []