# Напиши функцию, которая принимает два списка и
# возвращает список, содержащий элементы,
# которые присутствуют в обоих списках (пересечение).
# 
# Например, для входов [1, 2, 3] и [2, 3, 4] 
# результат должен быть [2, 3].


import pytest

from two_list_into_intersect.main import two_list_intersect

@pytest.mark.parametrize("input_data1, input_data2, expected", [
    (([1, 2, 3]), ([2, 3, 4]), [2, 3]),
    (([1, 2, 3]), ([]), [])
])
def test_two_list_intersect(input_data1, input_data2, expected):
    assert two_list_intersect(input_data1, input_data2) == expected