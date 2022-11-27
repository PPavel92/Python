# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#  ⋀ - and ⋁ - or ¬ - not

a = []
for _ in range(3):
    a.append(input(f"Введите значение : "))

left = not ([] or [] or [])
right = not [] and not [] and not []
result = left == right

if result == True:
    print("Утверждение истинна")
else:
    print("Утверждение ложь")
