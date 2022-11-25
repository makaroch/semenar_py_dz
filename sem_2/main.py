# Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# str = input('введите число ')
# summ = 0
# for i in str:
#     if i != ',' and i !='.':
#         summ += int(i)
# print(summ)

# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('введите число '))
# list = [1]
# for x in range(2,num + 1):
#     list.append(list[x-2] * x)
# print(list)

#Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# num = int(input('введите число '))
# list = []
# summ = 0
# for i in range(1,num+1):
#     n = round((1 + 1/i) ** i, 2)
#     summ += n
#     list.append(n)
# print(list)
# print("cумма чисел последовательности = ", summ)

#Реализуйте алгоритм перемешивания списка.
import random

list_1 = list(range(0,10))
print(list_1)
for i in range(len(list_1)):
    rand_num = random.randrange(0,10)
    list_1[i] , list_1[rand_num] = list_1[rand_num], list_1[i]
print(list_1)

# или вариант через готовый метод shuffle() 

list_2 = list(range(0,10))
print(list_2)
random.shuffle(list_2)
print(list_2)