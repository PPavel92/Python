# Реализуйте алгоритм перемешивания списка.


# import random
# list = [1,2,3,4,5,6,7,8,9,10]
# random.shuffle(list)
# print(list)


# list = [1,2,3,4,5,6,7,8,9,10]
# list.reverse()
# print(list)

list = [1,2,3,4,5,6,7,8,9,10]
f = -1 
for i in range(len(list)//2):
    list[f], list[i] = list[i], list[f]
    f -= 1
    print(list)