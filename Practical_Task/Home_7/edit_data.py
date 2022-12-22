from rewrite import rewrite
from print_data import print_data

def edit_data(seek_out, data):
   seek_out_res = {}
   for i in range(len(data)):
    if seek_out in data[i]:
        seek_out_res[i] = data[i]
    print(seek_out_res)
    while (key_:= int(input('Введите Id:_  '))) not in seek_out_res:
        print("Контакт с таким Id не наеден, ведите корректный Id: ") 
    else: 
        print('Какой раздел вы хотите изменить?')
        while (num := int(input('0 - first_name, 1 -last_name, 2- phone_number :_  '))) not in range(3):
            print('Не корректный ввод.')
        else:
            data[key_][num] = input('Введите данные: ')
    rewrite(data)