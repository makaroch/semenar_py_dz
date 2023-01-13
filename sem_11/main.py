# -*- coding: utf8 -*-


class MinMax:

    def __init__(self):
        self.list_obg = []

    def add_sent(self, text: str):
        text_list = text.split() # ff ff ffff
        self.list_obg.extend(text_list)

    def shorts(self):
        count = 999
        for item in self.list_obg:
            if len(item) < count: count = len(item)
        res_l = []
        for item in self.list_obg:
            if len(item) == count: res_l.append(item)
        res_l.sort()
        return res_l

    def long(self):
        count = 0
        for item in self.list_obg:
            if len(item) > count: count = len(item)
        res_l = []
        for item in self.list_obg:
            if len(item) == count: res_l.append(item)
        res_l.sort()
        return res_l

# min_max = MinMax()
# min_max.add_sent("vvvvv dd fjfj sfjsso osafj aofaojfa jf")
# print(min_max.shorts())
# print(min_max.long())

class TicTacToeBoard:

    def __init__(self):
        self.board_list = [['-', '-', '-'],
                           ['-', '-', '-'],
                           ['-', '-', '-']]

        self.list_win = [[(0, 0), (0, 1), (0, 2)],
                        [(1, 0), (1, 1), (1, 2)],
                        [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (1, 1), (2, 1)],
                        [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)],
                        [(0, 2), (1, 1), (2, 0)]]
        self.list_X = []
        self.list_0 = []
        self.X_go = True
        self.condition = None

    def new_gem(self):
        self.board_list = [['-', '-', '-'],
                           ['-', '-', '-'],
                           ['-', '-', '-']]
        self.list_X = []
        self.list_0 = []

    def get_field(self):
        for i in range(3):
            for j in range(3):
                print('|', end="")
                print(self.board_list[i][j], end="")
            print("|")
        print()

    def chek_field(self):
        return self.condition

    def make_move(self, row: int, col: int):

        def chek_win(char: str, char_list: list):
            if len(char_list) >= 3:
                for item in self.list_win:
                    win_count = 0
                    for i in range(len(char_list)):
                        if char_list[i] in item:
                            win_count += 1
                        if win_count == 3:
                            return char
                return None
            else:
                return None

        if 0 <= row < 3 and 0 <= col < 3 and self.board_list[row][col] == "-":
            if self.X_go:
                self.board_list[row][col] = "X"
                self.list_X.append((row, col))
                self.X_go = not self.X_go
            else:
                self.board_list[row][col] = "0"
                self.list_0.append((row, col))
                self.X_go = not self.X_go


            if len(self.list_X) + len(self.list_0) != 9:
                res = chek_win("X", self.list_X)
                if res is None:
                    res = chek_win("0", self.list_0)
                self.condition = res

                if res is None: return "Продолжаем играть"
                else: return f"Победил игрок {res}"
            else:
                self.condition = "D"
                return "Ничья"
        else: return "Некоректный ввод"




