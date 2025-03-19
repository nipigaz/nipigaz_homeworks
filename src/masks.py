import os
import logging

# Убедимся, что папка logs существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логирования для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/masks.log', encoding='utf-8')
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


def get_mask_card_number(card_number: str | int) -> str:
    """Убедимся, что номер карты строкового типа и маскируем номер кредитной карты, оставляя видимыми
    первые и последние четыре цифры."""
    logger.debug("Получение маскированного номера карты для: %s", card_number)

    card_number = str(card_number)

    # Проверка длины номера карты
    if len(card_number) != 16:
        logger.error("Неверная длина номера карты: %s", card_number)
        raise ValueError("Номер карты должен быть 16 символов.")
    if not card_number.isdigit():
        logger.error("Неверный формат номера карты: %s", card_number)
        raise ValueError("Номер карты должен состоять только из цифр.")

    # Формируем маску
    masked_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    logger.info("Маска номер карты: %s", masked_number)
    return masked_number


def get_mask_account(account_number: str | int) -> str:
    """Убедимся, что номер счета строкового типа и маскируем номер счета, оставляя видимыми только последние
    четыре цифры."""
    logger.debug("Получение маскированного номера счета для: %s", account_number)

    account_number = str(account_number)

    # Проверка длины номера счета
    if len(account_number) < 4:
        logger.error("Неверная длина номера счета: %s", account_number)
        raise ValueError("Номер счета должен иметь минимум 4 цифры.")

    # Формируем маску
    masked_account = "**" + account_number[-4:]
    logger.info("Маска номер счета: %s", masked_account)
    return masked_account
