# Задание 5: Фибоначчи
# Напишите функцию fibonacci(n), которая принимает целое неотрицательное число n и 
# возвращает n-е число Фибоначчи. 
# Последовательность Фибоначчи определяется следующим образом:

# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) для n > 1
# Например:

# fibonacci(0) должно вернуть 0
# fibonacci(1) должно вернуть 1
# fibonacci(5) должно вернуть 5 (поскольку последовательность выглядит так: 0, 1, 1, 2, 3, 5)

import pytest

from fibo.main import fibonacci

@pytest.mark.parametrize("input_data, expected", [
    (0, 0),
    (1, 1),
    (5, 5)
])
def test_fibonacci(input_data, expected):
    assert fibonacci(input_data) == expected
