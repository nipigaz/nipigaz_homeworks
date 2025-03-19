# tests/test_operations.py
from unittest.mock import patch, Mock
from src.utils import load_transactions
from src.external_api import convert_to_rub


def test_load_transactions_valid_file():
    """Проверяет загрузку транзакций из корректного JSON-файла."""
    with patch('builtins.open') as mock_file:
        mock_file.return_value.__enter__.return_value.read.return_value = '[{"id": 1}]'
        assert load_transactions('data/operations.json') == [{"id": 1}]


def test_load_transactions_invalid_file():
    """Проверяет возврат пустого списка при несуществующем файле или ошибке декодирования."""
    assert load_transactions('invalid_path.json') == []


@patch('src.external_api.requests.get')
def test_convert_to_rub_usd(mock_get):
    """Тестирует конвертацию USD в RUB с мокированным ответом API."""
    mock_response = Mock()
    mock_response.json.return_value = {'result': 75.5}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'USD'}
        }
    }
    assert convert_to_rub(transaction) == 75.5


def test_convert_to_rub_rub():
    """Проверяет, что сумма в RUB возвращается без изменений."""
    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'RUB'}
        }
    }
    assert convert_to_rub(transaction) == 100.0
