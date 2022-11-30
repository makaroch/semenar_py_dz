
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def Task1():
    some_list = [2, 3, 5, 9, 3, 5, 8, 3, 7]
    result = 0
    for i in range(1,len(some_list), 2):
        result += some_list[i]
    print(result)
Task1()


# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Task2():
    some_list = [2, 3, 5, 6]
    out_list = []
    if len(some_list) % 2 == 0:
        length = len(some_list) // 2
    else:
        length = len(some_list) // 2 + 1
    for i in range(length):
        out_list.append(some_list[i] * some_list[-1 - i]) 
    print(out_list)
Task2()
'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт 
разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
1.1 1.2 3.1 5 10.01
'''

# input_list = list(map(float, input('ВВЕДИТЕ ЧИСЛА ЧЕРЕЗ ПРОБЕЛ : \n').split()))
# output_list = [round((item % 1), 2) for item in input_list if item % 1 != 0]
# print(f'макимальная дробная часть = {max(output_list)}, минимальная дробная часть = {min(output_list)}, разность {round((max(output_list) - min(output_list)), 2)}  ')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input("введите десятичное число \n"))
# str_num_bin = ''
# while num !=0:
#     str_num_bin = str(num % 2) + str_num_bin
#     num = num // 2 
# print(str_num_bin)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
    #                                                                0   1        

# fib = [0, 1]
# num = int(input("введите десятичное число \n"))
# for i in range(2,num+1):
#     fib.append(fib[i-1] + fib[i-2])
# for _ in range(num):
#     x = fib[1] - fib[0]
#     fib.insert(0, x)
# print(fib)