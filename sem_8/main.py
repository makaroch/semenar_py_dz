import datetime
def rocket():
    '''
    Напишите программу для определения безопасных дат сближения с Солнцем в
    зависимости от наличия мозга.

    ЕСЛИ мозг есть, то каждое третье сближение безопасное (на двух предыдущих он
    успевает научиться). Если мозга нет, то безопасные только те сближения, что попадают
    на четверг.

    Формат ввода:
    Вводится начальная дата - последнее сближение с Солнцем (не рассматривается как
    подходящая).
    Затем вводится 1 или 0 - есть мозг или нет.
    Затем период обращения вокруг Солнца.
    Количество требуемых дат.

    Формат вывода:
    Выведите нужное количество ближайших дат безопасного сближения
    '''
    data_beginning = list(map(int, input("введите начальную дату - последнее сближение с Солнцем(день.месяцю.год через пробел) \n").split('.')))
    ii_on = int(input("введите 1 - ии есть или 0 - ии нет\n"))
    period = int(input('период обращения вокруг Солнца.\n'))
    data_caunt = int(input("Количество требуемых дат.\n"))
    d = datetime.date(data_beginning[2], data_beginning[1], data_beginning[0])
    print(d)
    d_new = d + datetime.timedelta(1)
    if ii_on:# хз что за пример с наличием мозга и как у них работает период
        print('ii_on')
        while d_new.weekday() != 3:
            d_new += datetime.timedelta(1)
        print(d_new.strftime('%d %B %Y'))
        d_new += datetime.timedelta(7)
        print(d_new.strftime('%d %B %Y'))
        for _ in range(data_caunt - 2):
            print('хз как тут работает переод')
    else:
        print('ii_of')
        while d_new.weekday() != 3:
            d_new += datetime.timedelta(1)
        for _ in range(data_caunt):
            print(d_new.strftime("%d %B %Y"))
            d_new += datetime.timedelta(period * 7)
# rocket()

import random
def rocket_2():
    '''
    Напишите программу, создающую несколько различных случайных ракет со случайным
    грузом на случайных траекториях.
    Номер ракеты - прописная буква латинского алфавита из заданного диапазона, две
    любые цифры, номер целиком не повторяется;
    Грузоподъёмность - целое число из заданного диапазона с шагом 50, повторения
    возможны;
    Дальность — вещественное число из заданного диапазона с точностью до одного знака
    после запятой, без повторений;
    Груз — случайная строка из заданного набора, без повторений.

    Формат ввода
    Вводятся:
    количество ракет,
    две буквы латинского алфавита через пробел — диапазон букв для номера, введённые
    буквы включаются в диапазон;
    Два целых числа через пробел - диапазон грузоподъёмности;
    два вещественных числа через пробел диапазон дальности;
    словосочетания через запятую и пробел — возможные грузы.
    '''
    rocket_count = int(input('введите кол-во ракет\n'))
    range_letters = input('введте 2 буквы через пробел \n').split()
    range_cargo = list(map(int, input('Два целых числа через пробел - диапазон грузоподъёмности\n').split()))
    range_distance = list(map(float, input('два вещественных числа через пробел диапазон дальности\n').split()))
    range_gruz = input('словосочетания через запятую и пробел — возможные грузы\n').split(', ')
    print(range_gruz)
    def numder_gener(range_let: list):
        name = ''
        name += chr(random.randint(ord(range_let[0]), ord(range_let[1])))
        name += str(random.randint(10, 100))
        return name

    def cargo_gen(range_carg: list):
        return random.randrange(range_carg[0], range_carg[1], 50)

    def distance_gen(range_distant):
        x = (random.uniform(range_distant[0], range_distant[1]))
        return (f'{x:.2f}')

    def gruz_gen(gruz_list: list):
        i = random.randint(0, len(gruz_list) - 1)
        return gruz_list[i]

    def main():
        set_name = set([])
        set_distance = set([])
        set_gruz = set([])

        for _ in range(rocket_count):

            name = numder_gener(range_letters)
            while name in set_name:
                name = numder_gener(range_letters)
            set_name.add(name)

            cargo = cargo_gen(range_cargo)

            distance = distance_gen(range_distance)
            while distance in set_distance:
                distance = distance_gen(range_distance)
            set_distance.add(distance)

            gruz = gruz_gen(range_gruz)
            while gruz in set_gruz:
                gruz = gruz_gen(range_gruz)
            set_gruz.add(gruz)

            print(f'Rocket {name} ({cargo}, {distance}) follows with cargo of {gruz}')
    main()
rocket_2()
