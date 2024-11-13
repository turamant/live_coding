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

import requests
from typing import List, Dict, Any

def fetch_and_process_data(url: str) -> List[Dict[str, Any]]:
    response = requests.get(url)
    response.raise_for_status()  # выбросит исключение для статусов 4xx и 5xx
    data = response.json()
    
    # Извлечение нужных полей
    processed_data = []
    for item in data:
        processed_item = {
            "id": item.get("id"),
            "name": item.get("name"),
            "email": item.get("email")
        }
        processed_data.append(processed_item)
    
    return processed_data
