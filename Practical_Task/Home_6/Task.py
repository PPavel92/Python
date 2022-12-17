# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


list_one = [1, 1, 2, 3, 4, 4, 4]

duplic = [i for i in list_one if list_one.count(i) == 1]
    
print(f"Список из неповторяющихся элементов: {duplic}")



# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 10.01]

new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(f"Разница между максимальным и минимальным значением дробной части => " , max(new_lst) - min(new_lst))


# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

m_str = str(input("Введите слова, через пробел: "))
filtered_list = list(filter(lambda lst: "абв" not in lst, m_str.split(" ")))
print(filtered_list)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = list(map(int, input("Введите числа через пробел:\n").split()))

l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
print(new_lst)

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

f_lst = '2, 3, 5, 9, 3, 1'
# sum = [lst[i]  for i in range(len(f_lst)) if i % 2 != 0 else list[i] +list[i]]
sum = list(filter(lambda i_lst: f_lst % 2 != 0 not in i_lst, f_lst))