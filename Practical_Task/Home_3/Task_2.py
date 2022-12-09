# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list =[2, 3, 4, 5, 6]

def sum_index(list):
    list_new =[]
    for i in range(len(list)//2 + 1 
    if len(list) % 2 != 0 
    else len(list)//2):
        sum_id =0
        sum_id = list[i] * list[-1-i]
        i += 1
        list_new.append(sum_id)
    return list_new
   
print(f"Произведение пар чисел списка: " , sum_index(list))