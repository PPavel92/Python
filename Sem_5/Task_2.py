# 2. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 5 6 7 9


with open("Sem_5_Task_2.txt", "r") as data:
    my_str = data.readline()
print(my_str)

my_list = my_str.split(" ")
last2 =[]
for i in range(0, len(my_list)- 1):
    my_list[i] = int(my_list[i])
    if int(my_list[i]) + 1 != int(my_list[i+1]):
        last2.append(my_list[i]+1)

print(last2)
   
