# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#  ⋀ - and ⋁ - or ¬ - not

a = []
for _ in range(3):
    a.append(input(f"Введите значение : "))

left = not ([0] or [1] or [2])
right = not [0] and not [1] and not [2]
result = left == right


if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
print(result)
print(left)
print(right)