def Task_1():
    '''
    Дан список интов, повторяющихся элементов в списке нет.
    Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
    Примеры
    :
    [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
    [1,4,3,2] => "1-4"
    [1,4] => "1,4"
    '''
    some_list = [1,4,3,7,8,10,11,12,20,19,23,81]
    some_list.sort()
    print(some_list)
    res = ""
    index_min = 0  # леваая граница интервала
    flag = True # отвечает за то что число одиночное
    for i in range(0, len(some_list) - 1):
        if some_list[i] == some_list[i+1] - 1: # проверка на то что числа идут подрят
            flag = False
        elif flag: # если число одиночное записываем только его
            res += str(some_list[i]) + ","
            index_min = i + 1
        else:  # иначе запишем интревал
            res += str(some_list[index_min]) + "-" + str(some_list[i]) + ","
            index_min = i + 1
            flag = True
        if i == len(some_list)-2:
            if flag:  # еси последнее число одинокое(как грустно звучит) записать его
                res += str(some_list[-1])
            else:  # иначе записать последний итервал или вообще все цифры в один интервал если index_min не изменился
                res += str(some_list[index_min]) + "-" + str(some_list[-1])
    print(res)

    
def Compress(file_name : str):
    with open(file_name,'r', encoding='utf-8') as file:
        string = file.readline()
    i = 0
    compress = ''
    if string != "":
        print(string)
        while i < len(string):
            count = 1
            while (i+1 < len(string)) and (string[i] == string[i+1]):
                count += 1
                i += 1
            if count == 1:
                compress += string[i]
            else:
                compress += string[i] + str(count)
            i += 1
        with open("compress_rle.txt", 'w+', encoding="utf-8") as file:
            file.writelines(compress)
    else:
        print("введена пустая строка")
Compress("decompress_rle.txt")
