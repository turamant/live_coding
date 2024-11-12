# Напиши функцию, которая принимает строку и возвращает количество гласных букв в этой строке.
#  Гласные буквы: 'a', 'e', 'i', 'o', 'u' (в любом регистре).

# Когда будешь готов, просто напиши свое решение!

import pytest

from vowels_in_string.main import count_vowels_in_string

@pytest.mark.parametrize("input_data, expected", [
    ("make", 2),
    ("congratilation", 6),
    ("The best", 2)
])
def test_count_vowels_in_string(input_data, expected):
    assert count_vowels_in_string(input_data) == expected