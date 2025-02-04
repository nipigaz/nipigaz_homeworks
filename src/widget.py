def mask_account_card(account_info: str) -> str:
    """
    Замаскировать номер банковской карты или счета.
    """
    if account_info.startswith("Счет "):
        # Обрабатываем счет
        account_number = account_info[5:]  # Убираем "Счет "
        if not account_number.isdigit() or len(account_number) < 4:
            raise ValueError("Номер счета должен содержать минимум 4 цифры.")
        masked_number = '**' + account_number[-4:]  # Маскируем все, кроме последних 4 цифр
        return f"Счет {masked_number}"
    else:
        # Обрабатываем карты
        card_parts = account_info.split()
        if len(card_parts) < 2:
            raise ValueError("Некорректный формат номера карты.")
        card_number = card_parts[-1]  # Получаем номер карты (последняя часть строки)
        if not card_number.isdigit() or len(card_number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр.")
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"  # Форматируем номер карты
        return f"{card_parts[0]} {masked_number}"  # Возвращаем с типом карты


def get_date(time_string: str) -> str:
    """
    Преобразует временную метку из строки в формат ДД.ММ.ГГГГ.
    """
    if not time_string or 'T' not in time_string:
        raise ValueError("Некорректный формат даты. Ожидается формат 'YYYY-MM-DDTHH:MM:SS.ssssss'.")
    try:
        date_str = time_string.split('T')[0]  # Берем только нужную часть даты
        year, month, day = date_str.split('-')
        return f"{day}.{month}.{year}"
    except (IndexError, ValueError):
        raise ValueError("Некорректный формат даты. Ожидается формат 'YYYY-MM-DDTHH:MM:SS.ssssss'.")


# Примеры работы функций
if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Пример использования маскирования карты
    print(mask_account_card("Счет 73654108430135874305"))  # Пример использования маскирования счета
    print(get_date("2024-03-11T02:26:18.671407"))  # Пример преобразования даты
