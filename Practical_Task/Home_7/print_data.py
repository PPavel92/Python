def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15))
        print("-"*65)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(15))
    else:
        print("Справочник пуст!")