# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = int(input("Введите координаты оси Х: "))
y = int(input("Введите координаты оси Y: "))

if (x > 0 and y > 0):
    print("Первая четверть")
elif (x < 0 and y > 0):
    print("Вторая четверть")
elif (x < 0 and y < 0):
    print("Третья четверть")
elif (x > 0 and y < 0):
    print("Четвертая четверть")
else:
    print("Введены не коректные координаты")
