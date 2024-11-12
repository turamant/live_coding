# Напиши функцию, которая принимает строку и возвращает количество уникальных слов в этой строке.
#  Игнорируй регистр и знаки препинания.
#  Например, для строки "Hello, world! Hello." результат должен быть 2.

import pytest

from unique_count_word.main import unique_word, clean_punctuation
@pytest.mark.parametrize("input_data, expected", [
    ("Hello, world! Hello", 2),
    ("", 0)
])
def test_unique_word(input_data, expected):
    assert unique_word(input_data) == expected


@pytest.mark.parametrize("input_data, expected", [
    ("Hello, world! Hello", "Hello world Hello"),
    ("", "")
])
def test_clean_punctuation(input_data, expected):
    assert clean_punctuation(input_data) == expected