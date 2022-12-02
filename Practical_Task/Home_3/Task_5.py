# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input("Введите число: "))

def fib_m(n):
    a, b = 0, 1
    result = [0]
    for i in range(n):
        a, b = b, a - b
        result.append(a)
    return result

def fib_p(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        a, b = b, a + b
        result.append(a)
    return result

result1 = []
result2 = []
result1 = fib_m(n)
result2 = fib_p(n)
result1 = result1[::-1]
print(result1 + result2)