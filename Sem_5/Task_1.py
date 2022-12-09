# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Я люблю Джавуабв абви Питон'
# 'Я люблю Питон'

my_str = 'Я люблю Джавуабв абви Питон'


#1
print(my_str.replace('абв', ''))



#2
last = my_str.split(" ")
my_list = []
for i in last:
    if "абв" not in i:
        my_list.append(i)
print(*my_list) 

#3
last = my_str.split(" ")
my_list= [i for i in last if "абв" not in i]
print(*my_list)   # " * " убирает скобки списка 

#4
filtered_list = list(filter(lambda word: "абв" not in word, my_str.split(" ")))
print(filtered_list)