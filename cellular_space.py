# This module creates a two-dimension cellular space
# Contributor: cmh
# 2019/05/14
# cell: 0.4m * 0.4m
# width: 12 cells    length: 26 cells

class Cell:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.static = None
        self.occupied = False

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def get_static(self):
        return self.static

def create_space1():
    cellular_space1 = [[Cell(x, y) for x in range(12)] for y in range(26)]
    cellular_space1[0][0].static = 0

    for line in cellular_space1:
        for cell in line:

            for dx, dy in [(0,1), (1,0), (1,1)]:
                try:
                    if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                        if dx == dy == 1:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,1)
                        else:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1,1)
                    else:
                        if dx == dy == 1:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static+1.4, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                        else:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static+1, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                except IndexError:
                    pass

            if cell.get_X() - 1 > 0:
                for dx,dy in [(-1,0), (-1,1)]:
                    try:
                        if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                            if dy == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1,1)
                        else:
                            if dy == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static+1.4, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static+1, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                    except IndexError:
                        pass

            if cell.get_Y() - 1 > 0:
                for dx, dy in [(0, -1), (1, -1)]:
                    try:
                        if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                            if dx == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1,1)
                        else:
                            if dx == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static + 1.4,cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static + 1,cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                    except IndexError:
                        pass

    maximum = max(cell.static for line in cellular_space1 for cell in line)
    for line in cellular_space1:
        for cell in line:
            cell.static = round(maximum - cell.static,1)

    for x,y in [(a,b) for a in range(3) for b in range(5,22,2)]:
        cellular_space1[y][x].static = 0

    for x,y in [(a,b) for a in range(4,8) for b in range(3,22,2)]:
        cellular_space1[y][x].static = 0

    for x,y in [(a,b) for a in range(9,12) for b in range(1,22,2)]:
        cellular_space1[y][x].static = 0

    for x,y in [(a,b) for a in range(4,8) for b in range(23,25)]:
        cellular_space1[y][x].static = 0

    return cellular_space1


def create_space2():
    cellular_space1 = [[Cell(x, y) for x in range(12)] for y in range(26)]
    cellular_space1[0][0].static = 0

    for line in cellular_space1:
        for cell in line:

            for dx, dy in [(0, 1), (1, 0), (1, 1)]:
                try:
                    if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                        if dx == dy == 1:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,1)
                        else:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1,1)
                    else:
                        if dx == dy == 1:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static + 1.4,cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                        else:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static + 1,cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                except IndexError:
                    pass

            if cell.get_X() - 1 > 0:
                for dx, dy in [(-1, 0), (-1, 1)]:
                    try:
                        if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                            if dy == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1,1)
                        else:
                            if dy == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static + 1.4,cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static + 1,cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                    except IndexError:
                        pass

            if cell.get_Y() - 1 > 0:
                for dx, dy in [(0, -1), (1, -1)]:
                    try:
                        if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                            if dx == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1,1)
                        else:
                            if dx == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static + 1.4,cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(min(cell.static + 1,cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),1)
                    except IndexError:
                        pass

    for line in cellular_space1:
        for cell in line:
            cell.y = 25 - cell.y

    cellular_space1.reverse()

    maximum = max(cell.static for line in cellular_space1 for cell in line)
    for line in cellular_space1:
        for cell in line:
            cell.static = round(maximum - cell.static,1)

    for x, y in [(a, b) for a in range(3) for b in range(5, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(4, 8) for b in range(3, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(9, 12) for b in range(1, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(4, 8) for b in range(23, 25)]:
        cellular_space1[y][x].static = 0

    return cellular_space1

# a = create_space1()
# c = create_space2()
# b= [cell.static for line in a for cell in line]
# print(b)
# d = [cell.static for line in c for cell in line]
# print(d)