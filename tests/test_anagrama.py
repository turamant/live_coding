# Задание 8: Проверка анаграмм
# Напишите функцию are_anagrams(s1, s2), которая принимает две строки s1 и s2 и возвращает True,
# если строки являются анаграммами (т.е. содержат одни и те же буквы в разном порядке),
# и False в противном случае. Игнорируйте регистр и пробелы.

# Примеры:

# are_anagrams("listen", "silent") должно вернуть True
# are_anagrams("hello", "world") должно вернуть False
# are_anagrams("A gentleman", "Elegant man") должно вернуть True


import pytest

from anagrama.main import are_anagrams

@pytest.mark.parametrize("input_data1, input_data2, expected", [
    (("listen"), ("silent"), True),
    (("hello"), ("world"), False),
    (("A gentleman"), ("Elegant man"), True)

])
def test_are_anagrams(input_data1, input_data2, expected):
    assert are_anagrams(input_data1, input_data2) == expected