# Напиши функцию, которая принимает два списка и
# возвращает список, содержащий элементы,
# которые присутствуют в обоих списках (пересечение).
# 
# Например, для входов [1, 2, 3] и [2, 3, 4] 
# результат должен быть [2, 3].


def two_list_intersect(numbers1: list[int]=None, numbers2: list[int]=None)-> list[int]:
    if numbers1 is None:
        numbers1 = []
    if numbers2 is None:
        numbers2 = []    
    numbers = set.intersection(set(numbers1), set(numbers2))
    return list(numbers)


if __name__ == '__main__':
    print("..[2, 3]..", two_list_intersect([1, 2, 3], [2, 3, 4]))
    print("..[1, 2, 3]..", two_list_intersect([1, 2, 3]))