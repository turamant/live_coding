# Напиши функцию, которая принимает список чисел и возвращает новый список,
#  содержащий только четные числа из исходного списка.


def even_numbers(numbers: list[int])-> list[int]:
    even_numbers_list = [x for x in numbers if x % 2 == 0]
    return even_numbers_list


if __name__ == '__main__':
    print("..4..", even_numbers([1,4,5,7,9]))
    print("2, 6, 6, 8, 10, 2", even_numbers([2, 6, 6, 8, 10, 2]))
    print("..[]..", even_numbers([1, 3, 5, 15]))