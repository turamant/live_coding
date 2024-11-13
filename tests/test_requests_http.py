# Напиши функцию, которая принимает URL-адрес API,
# возвращает данные в формате JSON и обрабатывает их.
# 
#  Функция должна выполнять следующие действия:

# Выполнить GET-запрос к указанному URL.
# Обработать полученные данные, извлекая определенные поля (например, id, name, email).
# Вернуть список словарей, содержащих только эти поля.

# API response:
# [
    # {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30},
    # {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25}
# ]

# function have to response:
# [
    # {"id": 1, "name": "John Doe", "email": "john@example.com"},
    # {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
# ]

# Условия:
# Используй стандартные библиотеки Python и библиотеку requests для выполнения HTTP-запросов.
# Обработай возможные ошибки, такие как ошибки сети или ошибки при парсинге JSON.


import pytest

from requests.exceptions import HTTPError
from requests_http.main import fetch_and_process_data

@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch('requests.get')

def test_successful_response(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
    ]
    
    url = "https://api.example.com/data"
    result = fetch_and_process_data(url)
    
    expected_result = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
    ]
    
    assert result == expected_result

def test_error_response(mock_requests_get):
    # Настраиваем мок так, чтобы он выбрасывал HTTPError при вызове raise_for_status
    mock_requests_get.return_value.status_code = 404
    mock_requests_get.return_value.raise_for_status.side_effect = HTTPError("Not Found")
    
    url = "https://api.example.com/data"
    
    with pytest.raises(HTTPError):
        fetch_and_process_data(url)

def test_invalid_json(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.side_effect = ValueError("Invalid JSON")
    
    url = "https://api.example.com/data"
    
    with pytest.raises(ValueError):
        fetch_and_process_data(url)