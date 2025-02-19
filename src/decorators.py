from functools import wraps


def log(filename: str | None = None) -> callable:
    """
    Декоратор для логирования выполнения функций.
    Логирует успешное выполнение или ошибки в консоль или файл.
    """

    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> any:
            """
            Обертка функции для логирования.

            """
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}\n"
                raise
            finally:
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message, end="")

        return wrapper

    return decorator
