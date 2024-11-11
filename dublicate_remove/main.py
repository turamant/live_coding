# Задание 4: Удаление дубликатов из списка
# Напишите функцию remove_duplicates(numbers), которая принимает список чисел и возвращает новый список,
# содержащий только уникальные элементы из исходного списка. Порядок элементов в новом списке должен
# соответствовать порядку их первого появления в исходном списке.
# 
#  Например:

# remove_duplicates([1, 2, 2, 3, 4, 4, 5]) должно вернуть [1, 2, 3, 4, 5]
# remove_duplicates([1, 1, 1, 1]) должно вернуть [1]


def remove_duplicates(numbers: list=None)-> list:
    if numbers == None:
        return []
    
    if not isinstance(numbers, list):
        raise ValueError("Входные данные должны быть списком")
    
    return list(set(numbers))

if __name__ == '__main__':
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    print(remove_duplicates([1, 1, 1, 1]))