# Задание 3:
# Напиши функцию, которая принимает строку и возвращает словарь,
# где ключами являются уникальные символы строки,
#  а значениями — количество их вхождений в строку.
# 
#  Например, для строки "hello" 
#  результат должен быть {'h': 1, 'e': 1, 'l': 2, 'o': 1}.


import pytest

from string_into_dict.main import string_to_dict

@pytest.mark.parametrize("input_data, expected", [
    ("hello", {'h': 1, 'e': 1, 'l': 2, 'o': 1}),
    ("hello world hero", {'h': 2, 'e': 2, 'l': 3, 'o': 3, 'w': 1, 'r': 2, 'd': 1} ),
    ("", {})
])
def test_string_to_dict(input_data, expected):
    assert string_to_dict(input_data) == expected