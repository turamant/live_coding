# Задание 1: Факториал числа
# Напишите функцию factorial(n), которая принимает целое неотрицательное число n и 
# возвращает его факториал. 
# Факториал числа n (обозначается как n!) — это произведение всех положительных целых чисел от 1 до n. 

# Например:

# factorial(0) должно вернуть 1
# factorial(5) должно вернуть 120 (поскольку 5! = 5 × 4 × 3 × 2 × 1)

def factorial(n: int)-> int:
    if n < 0:
        raise ValueError("n не может быть отрицательным!")
    if n < 2:
        return 1
    return n * factorial(n-1)


def factorial_non_recirsion(n: int)-> int:
    if n < 0:
        raise ValueError("n не может быть отрицательным")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result



if __name__ == '__main__':
    try:
        print(factorial(-9))
    except ValueError as e:
        print(e)
    print(factorial(0))
    print(factorial(5))
    print("==========")
    print(factorial_non_recirsion(-5))