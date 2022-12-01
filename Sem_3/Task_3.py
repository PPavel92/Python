# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# def fun():
#     list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
#     a = input('Введите число - ')
#     count = 0
#     for k in range(len(list)):
#         if list[k] == a:
#             count += 1
#             if count == 2:
#                 return k
#     return -1


# print(fun())


def func_1():
    list_a = ["123", "234", 123, "567"]
    find_char = "123"
    new_list = []
    for i in range(len(list_a)):
        if find_char == list_a[i]:
            new_list.append(i)
            if len(new_list) <= 1:
                return -1
    return new_list[1]

print(func_1())