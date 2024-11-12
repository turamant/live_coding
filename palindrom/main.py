# Напишите функцию is_palindrome(s), которая принимает строку s и возвращает True,
# если строка является палиндромом (читается одинаково слева направо и справа налево),
# и False в противном случае. Игнорируйте регистр и пробелы.

#  Например:

# is_palindrome("A man a plan a canal Panama") должно вернуть True
# is_palindrome("Hello") должно вернуть False


def is_palindrome(msg: str)-> bool:
    msg = msg.lower().replace(" ", "")
    return msg == msg[::-1]


if __name__ == '__main__':
    print(is_palindrome("A man a plan a canal Panama"))
    print(is_palindrome("Hello"))
   