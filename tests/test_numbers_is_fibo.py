# Напиши функцию, которая принимает список чисел и возвращает список,
# содержащий только числа Фибоначчи из этого списка.
# 
#  Например, для входа [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  результат должен быть [0, 1, 2, 3, 5, 8].


import pytest

from numbers_is_fibo.main import numbers_in_fibonacci


@pytest.mark.parametrize("input_data, expected", [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 5, 8]),
    ([], [])
])
def test_numbers_in_fibonacci(input_data, expected):
    assert numbers_in_fibonacci(input_data) == expected