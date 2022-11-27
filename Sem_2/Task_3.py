#  Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество вхождений одной строки в другой.
# 'Я люблю Python'
# 'лю'
# --> 2

# text = 'Я люблю Python'
# char = input('Введите значение поиска: ')
# len_char = len(char)
# i = 0
# count = 0
# while i < len(text)-1:
#     if char.lower() == text[i:len_char+i].lower():
#         count += 1
#     i += 1
# print(count)



# Через сплит.
text = 'Я люблю Python люблю'
searchText = input('Введите строку для подсчета вхождения: ')

list = text.split(searchText)
print(len(list)-1)


