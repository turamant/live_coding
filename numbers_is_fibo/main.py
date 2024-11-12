# Напиши функцию, которая принимает список чисел и возвращает список,
# содержащий только числа Фибоначчи из этого списка.
# 
#  Например, для входа [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  результат должен быть [0, 1, 2, 3, 5, 8].

def fibonacci(n: int) -> tuple:
    if n < 0:
        raise ValueError("Входное значение должно быть неотрицательным целым числом")
    
    fib_sequence = {0, 1}
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b 
        fib_sequence.add(b)
    
    return fib_sequence


def numbers_in_fibonacci(numbers: list[int]=None)-> list[int]:
    if numbers == None:
        numbers = []

    fibo_list = fibonacci(max(numbers, default=0))
    result_list = []
    for i in numbers:
        if i in fibo_list:
            result_list.append(i)
    
    return result_list


if __name__ == '__main__':
    print("..[0, 1, 2, 3, 5, 8]..", numbers_in_fibonacci([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print("..???..", numbers_in_fibonacci([]))