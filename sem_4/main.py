def Task_1():
    # Вычислить число c заданной точностью d
    # # Пример:
    # # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
    import math
    pi = math.pi
    rounding = "0.0001"
    print(round(pi, len(rounding) - 2))
# Task_1()
def Task_2():
    # Задайте натуральное число N. Напишите программу, 
    # которая составит список простых множителей числа N
    numb = int(input("Введите целое число: "))
    print("Простые:", end = " ")
    for i in range(numb - 1, 1, -1):
        count = 0 
        if (numb % i == 0):
            for j in range(i - 1, 1, -1):
                if (i % j == 0):
                    count = count + 1 # Увеличиваем, если находим делитель
            if (count == 0): # Если делителей не было найдено, выводим
                print(i, end = " ")
# Task_2()

def Task_3():
    # Задайте последовательность чисел. Напишите программу, 
    # которая выведет список неповторяющихся элементов исходной последовательности.
    some_list = [1, 5, 7, 2, 2, 3, 2, 2, 3]
    out_list = []
    for item_1 in some_list:
        count = 0
        for item_2 in some_list:
            if item_2 == item_1:
                count+=1
        if count == 1:
            out_list.append(item_1)  
    print(out_list)
# Task_3()
def Task_4():
    from random import randint
    step = int(input("введите число \n"))
    ratio_list = [randint(1, 100) for _ in range(step + 1)]
    print(ratio_list)
    str = ''
    for i in range(len(ratio_list)-1, -1, -1):
        if i > 1: str = str + f'{ratio_list[i]}*x^{i} + '
        elif i == 1: str = str + f'{ratio_list[i]}*x + '
        else: str = str + f'{ratio_list[i]}'
    Write(str)

def Write(text):
    with open('file33.txt', 'w', encoding="utf-8") as file:
        file.write(f'{text} \n')
Task_4()