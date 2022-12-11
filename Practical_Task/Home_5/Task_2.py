# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

#1

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите колличество конфет согласно условию: "))
#     return x


# def print_(name, f, counter, value):
#     print(f"Ходил {name}, он взял {f}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         f = input_dat(player1)
#         counter1 += f
#         value -= f
#         flag = False
#         print_(player1, f, counter1, value)
#     else:
#         f = input_dat(player2)
#         counter2 += f
#         value -= f
#         flag = True
#         print_(player2, f, counter2, value)

# if flag:
#     print(f"Выиграл(а) {player1}")
# else:
#     print(f"Выиграл(а) {player2}")



#2  Добавьте игру против бота 

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите колличество конфет согласно условию: "))
#     return x


# def print_(name, f, counter, value):
#     print(f"Ходил {name}, он взял {f}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя игрока: ")
# player2 = str("Бот<Вася>")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) 
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         f = input_dat(player1)
#         counter1 += f
#         value -= f
#         flag = False
#         print_(player1, f, counter1, value)
#     else:
#         f = randint(1, 28) 
#         f = f
#         counter2 += f
#         value -= f
#         flag = True
#         print_(player2, f, counter2, value)

# if flag:
#     print(f"Выиграл(а) {player1}")
# else:
#     print(f"Выиграл(а) {player2}")    


#3  Подумайте как наделить бота ""интеллектом""


from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите колличество конфет согласно условию: "))
    return x


def print_(name, f, counter, value):
    print(f"Ходил {name}, он взял {f}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя игрока: ")
player2 = str("Бот<Вася>")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        f = input_dat(player1)
        counter1 += f
        value -= f
        flag = False
        print_(player1, f, counter1, value)
    else:
        if value == 57:
            f = 1
        if 49 <= value <= 56:
            f = 20
        if value <= 48:
            f = randint(1, 3)
        if value <= 32:
            f = 1                    
        else:    
            f = randint(1, 28) 
        counter2 += f
        value -= f
        flag = True
        print_(player2, f, counter2, value)

if flag:
    print(f"Выиграл(а) {player1}")
else:
    print(f"Выиграл(а) {player2}")    
