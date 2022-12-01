# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['sdf13', 'fds66', '34']
# -> 3
# 'sdf13', '34'


a = ['sdf13', 'fds66', '34']

def in_a(a_, find_):
    result = False
    for i in a_:
        if find_ in i:
            result = True
            print(i)
    return result

print(in_a(a, "3"))          


a = ['sdf13', 'fds66', '34']

def find_idx(a_, find_):
    for i in range(len(a_)):
        if a_[i].find(find_) > -1:
            return i   
    
print(find_idx(a, "s"))  