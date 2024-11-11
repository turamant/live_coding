# Напишите функцию is_palindrome(s), которая принимает строку s и возвращает True,
# если строка является палиндромом (читается одинаково слева направо и справа налево),
# и False в противном случае. Игнорируйте регистр и пробелы.

#  Например:

# is_palindrome("A man a plan a canal Panama") должно вернуть True
# is_palindrome("Hello") должно вернуть False

from palindrom.main import is_palindrome

def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Hello") == False