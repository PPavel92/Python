# Считать строку из набора чисел из файла. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел. Результат заисать в конец исходного файла (х1 х2).

with open('test.txt', 'w') as data:
    data.write(f'2 5 7 10 3\n')
with open('test.txt', 'r') as data:
    lst = data.read()
new_lst = lst.split(' ')
lst_int = [int(i) for i in new_lst]
max_num = max(lst_int)
min_num = min(lst_int)

with open('test.txt', 'a') as data:
    data.write(f'max = {max_num} \n')
    data.write(f'min = {min_num} \n')
