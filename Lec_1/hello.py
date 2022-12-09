# типы данных и переменная
# int, float, boolean, str, list, None
# value = None
# a = 132
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello world'

# print(s)  # вывод строки
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3', 'hello', 1, 2, 4.5, True]
# print(list)

# Ввод и вывод данных
# print() - отвечает за вывод данных
# input() - отвечает за ввод данных

#print('Введите a');
#a = input()
#print('Введите b');
#b = input()
#print(a, b)
#print('{} {}'.format(a, b))
#print(f'{a} {b}')

# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a,'+', b, '=', a+b)

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a,'+', b, '=', a+b)


# Арифметические операции
# +,-,*,/,%,//,**
# (), Сокращенные операции
# a = 1.2
# b = 3
# c = a * b  # c = round(a * b, 5)
# print(c)

# a = 3
# a *= 5  # вместо a = a + 5

# print(a)

#  Логичесские операции
#  >, >=, <, <=, ==, !=
#  768   

# a = 1 > 4
# print(a)

# func = 1
# T = 4
# x = 3
# print(func < T > (x))

# f = 1 > 2 or 4 < 6
# print(f)

# f =[1,2,3,4]
# print(f)
# print(not 2 in f)
# is_odd = f[0] % 2 == 0
# print(is_odd)


# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if  a > b:
#     print(a)
# else:
#         print(b) 

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар -топ')
# else:
#     print('Привет, ', username)


# Управляющий модуль
# while, for

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


# # Управляющие конструкции:
# # for

# list = range(10)            #[1,32,3,5]
# for i in list:              # for i in range(1, 5): "без объявления List"
#     print(i)

     # начало, конец, шаг
# range(start, stop, step)
# range(5) -> [0, 1, 2, 3, 4]
# range(2, 5) -> [2, 3, 4]
# range(1, 7, 2) -> [1, 3, 5]


a = [1,2,3,5,8,15,23,38]
def gg(x):
   return x**2

g = [(i, gg(i)) for i in a if not i % 2]
print(g)