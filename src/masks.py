def get_mask_card_number(card_number: str | int) -> str:
    """Убедимся, что  номер карты строкового типа и маскируем номер кредитной карты, оставляя видимыми
    первые и последние четыре цифры."""
    card_number = str(card_number)

    # Проверяем длину номера карты (должна быть 16 символов)
    if len(card_number) != 16:
        raise ValueError("Номер карты должен быть 16 символов.")
    if not card_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр.")

    # Формируем маску
    masked_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    return masked_number



def get_mask_account(account_number: str | int) -> str:
    """Убедимся, что номер счета строкового типа и маскируем номер счета, оставляя видимыми только последние
     четыре цифры."""
    account_number = str(account_number)

    # Проверим, что номер счета достаточно длинный
    if len(account_number) < 4:
        raise ValueError("Номер счета должен иметь минимум 4 цифры.")

    # Формируем маску
    masked_account = "**" + account_number[-4:]

    return masked_account


# Пример использования
#print(get_mask_card_number("7000792289606361"))

# Пример использования
# print(get_mask_account("73654108430135874305"))
