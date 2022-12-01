# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# n = int(input("Введите число: "))
# fib1 = 1
# fib2 = 0

# i = 0
# while i < n :
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1
#     print(fib2)
# list = []
# data = list(fib2)
# print(data)

# не доделал

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        

data = list(fibonacci(8))
print(data)
