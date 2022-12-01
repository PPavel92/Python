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


test_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(f"список: {test_list}")
test_item = input("Введите искомую строку: ")


def check_list(test_list, test_item):
    count = 0
    for i in range(len(test_list)):
        if test_list[i] == test_item:
            count += 1
            if count == 2:
                return i
    else:
        return -1


print(f"ответ: {check_list(test_list, test_item)}")
