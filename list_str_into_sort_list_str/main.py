# Напиши функцию, которая принимает список строк и возвращает список строк,
# отсортированных по длине.
# Если длины строк одинаковы, строки должны быть отсортированы в алфавитном порядке.
# Например, для входа ["apple", "banana", "fig", "grape"] 
# результат должен быть ["fig", "apple", "grape", "banana"].

def convert_string(list_string: list[str])-> list[str]:
    str_list = []
    for i in list_string:
        str_list.append(i)
    return sorted(str_list, key=lambda x: (len(x), x))


if __name__ == '__main__':
    print('..["fig", "apple", "grape", "banana"]..', convert_string(["grape", "banana", "fig", "apple"]))
    print("...", convert_string(["apple", "", " ", "Grape"]))


        
