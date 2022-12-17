# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


m_str = str(input("Введите слова, через пробел: "))
last = m_str.split(" ")
my_list = []
for i in last:
    if "абв" not in i:
        my_list.append(i)
print(*my_list) 


# my_list = [ i for i in last if "абв" not in i,  my_list.append(i)]