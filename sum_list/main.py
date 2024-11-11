# Задание 3: Сумма чисел в списке
# Напишите функцию sum_of_list(numbers), которая принимает список чисел и возвращает их сумму.
# 
#  Например:

# sum_of_list([1, 2, 3, 4]) должно вернуть 10
# sum_of_list([-1, 1, 0]) должно вернуть 0


def sum_of_list(spisok: list=None)-> int:
    if spisok == None:
        return 0
    
    if not isinstance(spisok, list):
        raise ValueError("Входные данные должны быть списком")

    return sum(spisok)