# Задание 3:
# Напиши функцию, которая принимает строку и возвращает словарь,
# где ключами являются уникальные символы строки,
#  а значениями — количество их вхождений в строку.
# 
#  Например, для строки "hello" 
#  результат должен быть {'h': 1, 'e': 1, 'l': 2, 'o': 1}.


def string_to_dict(string: str)-> dict[str, int]:
    string = string.replace(" ", "")
    result_dict: dict[str, int] = {}

    for i in string:
        result_dict[i] = result_dict.get(i, 0) + 1
 
    return result_dict


if __name__ == '__main__':
    print(string_to_dict("hello"))
    print(string_to_dict("hello world hero"))
    print(string_to_dict(""))