# Задание 3: Сумма чисел в списке
# Напишите функцию sum_of_list(numbers), которая принимает список чисел и возвращает их сумму.
# 
#  Например:

# sum_of_list([1, 2, 3, 4]) должно вернуть 10
# sum_of_list([-1, 1, 0]) должно вернуть 0

import pytest

from sum_list.main import sum_of_list

@pytest.mark.parametrize("input_data, expected", [
    ([1, 2, 3, 4], 10),
    ([-1, 1, 0], 0),
    ([], 0),
    ([1.1, 2.3, 4.5], 7.9)

])
def test_sum_of_list(input_data, expected):
    assert sum_of_list(input_data) == expected
    

def test_sum_of_list_invalid_data():
    with pytest.raises(ValueError, match="Входные данные должны быть списком"):
        sum_of_list("ertyui")

    with pytest.raises(ValueError, match="Входные данные должны быть списком"):
        sum_of_list(12345)
    