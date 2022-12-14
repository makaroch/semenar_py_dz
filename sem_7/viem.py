def inpyt_in_or_out():
    i = input("введите 1 - запись или 0 - поиск \n")
    return i

def inpyt():
    form1 = input("введите нового человека\n")
    return form1

def out():
    form = input("введите кого ищем) \n")
    return form
def print_search(data):
    print(f' результаты поиска \n')
    for item in data:
        print(item)