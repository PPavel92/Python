

def rewrite(data):
    lst = []
    for i in range(len(data)):
        lst.append('\n'.join(data[i]))
    f = '\n\n'.join(lst)
    with open('phone.csv', 'r+') as file:
        file.write(f)
       