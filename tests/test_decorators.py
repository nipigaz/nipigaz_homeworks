import pytest

from src.decorators import log


def test_log_to_console_ok(capsys: pytest.CaptureFixture) -> None:
    """Проверка логирования успешного выполнения в консоль."""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    assert add(1, 2) == 3
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_to_console_error(capsys: pytest.CaptureFixture) -> None:
    """Проверка логирования ошибки в консоль."""

    @log()
    def fail() -> None:
        raise ValueError("Oops")

    with pytest.raises(ValueError):
        fail()

    captured = capsys.readouterr()
    assert "fail error: ValueError. Inputs: (), {}\n" in captured.out


def test_log_to_file_ok(tmp_path: pytest.TempPathFactory) -> None:
    """Проверка записи логов об успехе в файл."""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a: int, b: int) -> int:
        return a * b

    assert multiply(3, 4) == 12
    content = log_file.read_text(encoding="utf-8")
    assert content == "multiply ok\n"


def test_log_to_file_error(tmp_path: pytest.TempPathFactory) -> None:
    """Проверка записи логов об ошибке в файл."""
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def raise_error() -> None:
        raise TypeError("Invalid type")

    with pytest.raises(TypeError):
        raise_error()

    content = log_file.read_text(encoding="utf-8")
    assert "raise_error error: TypeError. Inputs: (), {}\n" in content


def test_exception_propagates() -> None:
    """Проверка, что исключение пробрасывается после логирования."""

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
