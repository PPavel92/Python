# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 10.01]
new_list = [(lst[i]* 100) % 100 for i in range(len(lst))]

def max_ind(new_list): 
    max_ = new_list[0]
    for i in new_list:
        if i > max_:
           max_ = i
    return max_ 

resalt_max = max_ind(new_list)


def min_ind(new_list): 
    min_ = new_list[0]
    for i in new_list:
        if i < min_:
           min_ = i
    return min_ 
    
resalt_min = min_ind(new_list)

print(f"Разница между максимальным и минимальным значением дробной части => " , (resalt_max-resalt_min)/100)