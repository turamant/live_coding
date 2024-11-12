# Напиши функцию, которая принимает строку и возвращает количество уникальных слов в этой строке.
#  Игнорируй регистр и знаки препинания.
#  Например, для строки "Hello, world! Hello." результат должен быть 2.

import string

def clean_punctuation(s: str)-> str:
    for char in string.punctuation:
        s = s.replace(char, '')
    return s
 
def unique_word(msg: str) -> int:
    msg = clean_punctuation(msg)
    msg = set(msg.split())
    
    return len(msg)


if __name__ == '__main__':
    print("..2..", unique_word("Hello, world! Hello."))
    print("..7..", unique_word("Hello, world! Hello, list my Hero. A Hero boys,!"))
    print("..0..", unique_word(""))

    


