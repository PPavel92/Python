from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data
from edit_data import edit_data 
from remov_data import remov_data
from rewrite import rewrite

    

def Phonebook():
    print("|**** Телефонный справочник ****|")


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    return [last_name, first_name, phone_number]
    
  
def choice_sep():
    sep = None
    return sep


def choice_do():
    print("  ----  Справочное меню:\n\
    1 - Добавить\n\
    2 - Экспорт\n\
    3 - Поиск контактаn\n\
    4 - Редактировать\n\
    5 - Удлить контакт")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    elif ch == '4':
        seek_out = input("Введите данные для поиска: ")
        data = export_data()
        edit_data(seek_out, data)
        
    elif ch == '5':
        seek_out = input("Введите данные для поиска: ")
        data = export_data()
        remov_data(seek_out, data)
        print(data)
    else:
        seek_out = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(seek_out, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15),)   
        else:
            print("Данные не обнаружены")
            choice_do()


   
