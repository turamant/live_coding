# Задание 4: Удаление дубликатов из списка
# Напишите функцию remove_duplicates(numbers), которая принимает список чисел и возвращает новый список,
# содержащий только уникальные элементы из исходного списка. Порядок элементов в новом списке должен
# соответствовать порядку их первого появления в исходном списке.
# 
#  Например:

# remove_duplicates([1, 2, 2, 3, 4, 4, 5]) должно вернуть [1, 2, 3, 4, 5]
# remove_duplicates([1, 1, 1, 1]) должно вернуть [1]

import pytest
from dublicate_remove.main import remove_duplicates


@pytest.mark.parametrize("input_data, expected", [
    ([1, 2, 2, 3, 4, 4, 5], [1,2,3,4,5]),
    ([1, 1, 1, 1], [1])
])
def test_remove_duplicates(input_data, expected):
    assert remove_duplicates(input_data)  == expected


def test_remove_duplicates_invalid_data():
    with pytest.raises(ValueError, match="Входные данные должны быть списком"):
        remove_duplicates("ertyui")

    with pytest.raises(ValueError, match="Входные данные должны быть списком"):
        remove_duplicates(12345)


