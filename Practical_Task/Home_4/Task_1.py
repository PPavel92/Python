# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
# Вывод: 3.14

# Ввод: 0.001
# Вывод: 3.141


def calc_pi(eps=1.0e-5):
    s=0
    d=1
    sgn=1
    while True:
        a=4/d
        s=s+sgn*a
        if a<eps:
            return s
        sgn=-sgn
        d=d+2
 
 
print(calc_pi())

# Вариант №2

# from math import pi

# d =  float(input("Введите число для заданной точности числа Пи:\n"))
# # print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
# resalt = pi
# print(resalt)