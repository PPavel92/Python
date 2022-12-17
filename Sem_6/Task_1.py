# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*

# 2+2 => 4;

# 1+2*3 => 7;

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

# *Пример:*

# 1+2*3 => 7;

# (1+2)*3 => 9;

# string = '10+200*3'

# lst = []
# buf = ''
# for i in range(len(string)):
#     if string[i].isdigit():
#         buf += string[i]
#     else:
#         lst.append(int(buf))
#         lst.append(string[i])
#         buf = ''
# else:
#     lst.append(int(buf))
# print(lst)


# while ('*' in lst) or ('/' in lst):
#     mult = -1
#     if '*' in lst:
#         mult = lst.index('*')

#     div = -1
#     if '/' in lst:
#         div = lst.index('/')

#     if ((mult < div) and (mult != -1) and (div != -1)) or ((mult != -1) and (div == -1)):
#         res = lst[mult - 1] * lst[mult + 1]
#         lst = lst[:mult - 1] + [res] + lst[mult + 2:]
#     elif (div < mult) and (div != -1) and (mult != -1) or ((div != -1) and (mult == -1)):
#         res = lst[div - 1] / lst[div + 1]
#         lst = lst[:div - 1] + [res] + lst[div + 2:]


# while ('+' in lst) or ('-' in lst):
#     plus = -1
#     if '+' in lst:
#         plus = lst.index('+')

#     minus = -1
#     if '-' in lst:
#         minus = lst.index('-')

#     if ((plus < minus) and (plus != -1) and (minus != -1)) or ((plus != -1) and (minus == -1)):
#         res = lst[plus - 1] + lst[plus + 1]
#         lst = lst[:plus - 1] + [res] + lst[plus + 2:]
#     elif (minus < plus) and (minus != -1) and (plus != -1) or ((minus != -1) and (plus == -1)):
#         res = lst[minus - 1] - lst[minus + 1]
#         lst = lst[:minus - 1] + [res] + lst[minus + 2:]

# print(lst)


# 2

# def serch(lst):
#     for x in range(len(lst)):

#         if '*' or '/' in lst[x]:
#             resalt = int(lst[lst.index('*') - 1]) * \
#                 int(lst[lst.index('*') + 1])
#             lst.pop([lst.index('*') - 1])
#             lst.pop([lst.index('*') + 1])
#             lst[lst.index('*')] = resalt


#     if lst.index('*') > 0:
#         if lst.index('/') > 0:
#             if lst.index('*') < lst.index('/'):
#                 resalt = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
#                 lst.pop([lst.index('*') - 1])
#                 lst.pop([lst.index('*') + 1])
#                 lst[lst.index('*')] = resalt
#             else:
#                 resalt = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
#                 lst.pop([lst.index('/') - 1])
#                 lst.pop([lst.index('/') + 1])
#                 lst[lst.index('/')] = resalt

#         else:
#             resalt = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
#             lst.pop([lst.index('*') - 1])
#             lst.pop([lst.index('*') + 1])
#             lst[lst.index('*')] = resalt
#     elif lst.index('/') > 0:
#         resalt = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
#         lst.pop([lst.index('/') - 1])
#         lst.pop([lst.index('/') + 1])
#         lst[lst.index('/')] = resalt

#    # else:
#    #     resalt = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
#    #     lst.pop(lst[lst.index('/') - 1])
#    #     lst.pop(lst[lst.index('/') + 1])
#    #     lst[lst.index('/')] = resalt
#    # if lst.index('*') > 0 or lst.index('/') > 0:
#    #     if (-1 !=lst.index('*')) and (lst.index('*') < lst.index('/')):
#    #         resalt = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
#    #         lst.pop(lst[lst.index('*') - 1])
#    #         lst.pop(lst[lst.index('*') + 1])
#    #         lst[lst.index('*')] = resalt
#    # else:
#    #     resalt = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
#    #     lst.pop(lst[lst.index('/') - 1])
#    #     lst.pop(lst[lst.index('/') + 1])
#    #     lst[lst.index('/')] = resalt
#    # print(lst)




# # r = lst.index('/')
# # print(r)

# str = input('Введите выражение (через пробелы между знаками) - ').split()
# serch(str)
# 4 *print(str)