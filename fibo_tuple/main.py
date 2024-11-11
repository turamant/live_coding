def fibonacci(n: int) -> tuple:
    if n < 0:
        raise ValueError("Входное значение должно быть неотрицательным целым числом")
    
    fib_sequence = []
    
    for i in range(n + 1):
        if i == 0:
            fib_sequence.append(i)
        elif i == 1:
            fib_sequence.append(i)
        else:
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    
    return tuple(fib_sequence)


if __name__ == '__main__':
    print(fibonacci(10))