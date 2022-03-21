# Вы загадали натуральное число ﻿n﻿ и решили заполнить квадратную таблицу размером ﻿n×n﻿ буквами по «диагональному правилу» 
# — клетки, находящиеся на двух самых длинных диагоналях, должны содержать символ «﻿a﻿». 
# Пустые клетки, соседние с «a﻿»-клетками, нужно заполнить символом «b», и так далее по алфавиту. 
# Когда придет время заполнять соседей «z﻿»-клеток, в них нужно записать символ «﻿a﻿». 
# Напишите программу, которая выведет получившуюся таблицу.

# Формат входных данных

# Входные данные содержат одно целое число ﻿n﻿ (﻿1 ≤ n ≤ 100) — высоту и ширину таблицы.

from pprint import pprint

#n = input()
#n = int(n)

class Liner:

    def __init__(self, side):
        self.side = side
        self.matrix = []
        self.line = 0
        self.unit = 0
        self.sided = 0

    def matrix_creator(self):
        for line in range(self.side):
            self.matrix.append([])
            for unit in range(self.side):
                self.matrix[line].append('')

        for i in range(self.side):
            self.matrix[i][i] = 'a'
            self.matrix[i][self.side-i-1] = 'a'

    def empty_searcher(self):
        for line in range(self.side):
            for unit in range(self.side):
                if self.matrix[line][unit] == '':
                    self.line = line
                    self.unit = unit
        return None

    def side_checker(self):
        if self.empty_searcher():
            if self.unit>0:
                self.sided = self.matrix[self.line][self.unit-1]
            elif self.unit<self.side-1:
                self.sided = self.matrix[self.line][self.unit+1]

    def engine(self):

        self.matrix_creator()

        while self.empty_searcher() != None:
            self.side_checker()
            if self.sided == 'z':
                self.matrix[self.line][self.unit] = 'a'
            else:
                self.matrix[self.line][self.unit] = chr(ord(self.side)+1)

        pprint(self.matrix)

m5 = Liner(side = 5)
m5.engine()