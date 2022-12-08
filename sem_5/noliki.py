maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps(map : list):
    print("--------------")
    for i in range(0, len(map), +3):
        print('|' ,map[i], ' | ', map[i +1], ' | ', map[i + 2], ' |')

def step_maps(step, symbol):
    maps[step - 1] = symbol

def get_result():
    win = ''
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
           win = 'X'
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
           win = "O"
    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    print_maps(maps)

    if player1 == True:
        symbol = "X"
        flagX = True
        while flagX:
            step = int(input("кожанный мешок №1, ваш ход: "))
            if 1 <= step <= 9:
                flagX = False
            else: print("некоректно, введите число от 1 до 9")
    else:
        symbol = "O"
        flagX = True
        while flagX:
            step = int(input("кожанный мешок № 2, ваш ход: "))
            if 1 <= step <= 9 :
                flagX = False
            else:
                print("некоректно, введите число от 1 до 9")

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not player1

print_maps(maps)
print("Победил", win)