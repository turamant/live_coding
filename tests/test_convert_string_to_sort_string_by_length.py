# Напиши функцию, которая принимает список строк и возвращает список строк,
# отсортированных по длине.
# Если длины строк одинаковы, строки должны быть отсортированы в алфавитном порядке.
# Например, для входа ["apple", "banana", "fig", "grape"] 
# результат должен быть ["fig", "apple", "grape", "banana"].


import pytest

from list_str_into_sort_list_str.main import convert_string

@pytest.mark.parametrize("input_data, expected", [
    (["apple", "banana", "fig", "grape"], ["fig", "apple", "grape", "banana"]),
    (["apple", "", " ", "Grape"], ['', ' ', 'Grape', 'apple'])

])
def test_convert_string(input_data, expected):
    assert convert_string(input_data) == expected