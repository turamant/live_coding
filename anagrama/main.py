# Задание 8: Проверка анаграмм
# Напишите функцию are_anagrams(s1, s2), которая принимает две строки s1 и s2 и возвращает True,
# если строки являются анаграммами (т.е. содержат одни и те же буквы в разном порядке),
# и False в противном случае. Игнорируйте регистр и пробелы.

# Примеры:

# are_anagrams("listen", "silent") должно вернуть True
# are_anagrams("hello", "world") должно вернуть False
# are_anagrams("A gentleman", "Elegant man") должно вернуть True


def are_anagrams(word1: str, word2: str)-> bool:
    word1 = sorted(word1.replace(" ", "").lower())
    word2 = sorted(word2.replace(" ","").lower())
    if word1 == word2:
        return True
    return False


if __name__ == '__main__':
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("hello", "world"))
    print(are_anagrams("A gentleman", "Elegant man"))