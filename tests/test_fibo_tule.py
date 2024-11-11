import pytest
from fibo_tuple.main import fibonacci

@pytest.mark.parametrize("input_data, expected", [
    (0, (0,)),
    (1, (0, 1,)),
    (5, (0, 1, 1, 2, 3, 5,))
])
def test_fibonacci(input_data, expected):
    assert fibonacci(input_data) == expected
