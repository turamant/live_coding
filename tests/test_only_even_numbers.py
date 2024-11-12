# Напиши функцию, которая принимает список чисел и возвращает новый список,
#  содержащий только четные числа из исходного списка.


import pytest

from even_numbers.main import even_numbers


@pytest.mark.parametrize("input_data, expected", [
    ([1,4,5,7,9], [4]),
    ([2, 6, 6, 8, 10, 2], [2, 6, 6, 8, 10, 2]),
    ([1, 3, 5, 15], []),
])
def test_even_numbers(input_data, expected):
    assert even_numbers(input_data) == expected

    