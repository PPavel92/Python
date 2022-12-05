# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   

d =  float(input("Введите число для заданной точности числа Пи: "))
def calc_pi(d):
    s=0
    f=1
    b=1
    while True:
        a=4/f
        s=s+b*a
        if a<d:
            return s
        b=-b
        f=f+2
print(f'Число Пи с заданной точностью {d} равно {round(calc_pi(d), 3)}')


