# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3, 5, 9, 3, 5, 1]

def sum_index(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    print("Сумма нечетных индексов равна: ", sum)

sum_index(list)