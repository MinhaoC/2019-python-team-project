from random import randrange, random
from math import e
from graphics import *

class Button:
    def __init__(self,win,center,width,height,label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin,self.ymin)
        p2 = Point(self.xmax,self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)
        self.label = Text(center,label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self,p):
        return (self.active and self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

class InputDialog:
    def __init__(self,number,weigh):
        self.win = win = GraphWin('Evacuee Number', 200, 300)
        win.setCoords(0,4.5,4,.5)

        Text(Point(2, 1), 'Disaster is coming!').draw(win)

        Text(Point(1,2),'Number').draw(win)
        self.number = Entry(Point(3,2),5)
        self.number.draw(win)
        self.number.setText(str(number))

        Text(Point(1,3),'Weigh').draw(win)
        self.weigh = Entry(Point(3,3), 5)
        self.weigh.draw(win)
        self.weigh.setText(str(weigh))

        self.simulate = Button(win,Point(1,4),1.4,.5,"Simulate!")
        self.simulate.activate()

        self.quit = Button(win,Point(3,4),1.4,.5,'Quit')
        self.quit.activate()

    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return 'Quit'
            if self.simulate.clicked(pt):
                return 'Simulate!'

    def getValues(self):
        n = float(self.number.getText())
        wg = float(self.weigh.getText())
        return n,wg

    def close(self):
        self.win.close()

class Classroom:
    def __init__(self):
        self.win = GraphWin('Classroom 105', 320, 520, autoflush=False)
        self.win.setCoords(11.5,-0.5,-0.5,25.5)


    def draw_cell_vertical_line(self):
        for i in range(12):
            line = Line(Point(i-0.5,-0.5),Point(i-0.5,25.5))
            line.draw(self.win)
        line = Line(Point(11.5,-0.5),Point(11.5,25.5))
        line.draw(self.win)

    def draw_cell_horizontal_line(self):
        for i in range(26):
            line = Line(Point(-0.5,i-0.5),Point(11.5,i-0.5))
            line.draw(self.win)
        line = Line(Point(-0.5,25.5),Point(11.5,25.5))
        line.draw(self.win)

    def fill_green(self):
        for y in range(5,22,2):
            for x in range(1,3):
                rec = Rectangle(Point(x+0.5,y-0.5),Point(x-0.5,y+0.5))
                rec.setFill('green')
                rec.draw(self.win)

        for y in range(3,22,2):
            for x in range(4,8):
                rec = Rectangle(Point(x+0.5,y-0.5),Point(x-0.5,y+0.5))
                rec.setFill('green')
                rec.draw(self.win)

        for y in range(1,22,2):
            for x in range(9,12):
                rec = Rectangle(Point(x+0.5,y-0.5),Point(x-0.5,y+0.5))
                rec.setFill('green')
                rec.draw(self.win)

        for y in range(23,25):
            for x in range(4,8):
                rec = Rectangle(Point(x+0.5,y-0.5),Point(x-0.5,y+0.5))
                rec.setFill('green')
                rec.draw(self.win)

    def draw_doors(self):
        door1 = Rectangle(Point(0.5,-0.5),Point(-0.5,0.5))
        door1.setFill('red')
        door1.draw(self.win)
        door2 = Rectangle(Point(0.5, 24.5), Point(-0.5, 25.5))
        door2.setFill('red')
        door2.draw(self.win)

    def turn_orange(self,x,y):
        rec = Rectangle(Point(x+0.5,y-0.5),Point(x-0.5,y+0.5))
        rec.setFill('orange')
        rec.draw(self.win)

    def turn_off_orange(self,x,y):
        rec = Rectangle(Point(x + 0.5, y - 0.5), Point(x - 0.5, y + 0.5))
        rec.setFill('white')
        rec.draw(self.win)

    def draw_evacuee(self,evacuee):
        self.turn_orange(evacuee.get_X(),evacuee.get_Y())

    def undraw_evacuees(self,evacuee):
        self.turn_off_orange(evacuee.get_X(),evacuee.get_Y())


class Cell:

    def __init__(self, x, y):
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

    def is_occupied(self):
        self.occupied = True

    def not_occupied(self):
        self.occupied = False


def create_space1():
    cellular_space1 = [[Cell(x, y) for x in range(12)] for y in range(26)]
    cellular_space1[0][0].static = 0

    for line in cellular_space1:
        for cell in line:

            for dx, dy in [(0, 1), (1, 0), (1, 1)]:
                try:
                    if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                        if dx == dy == 1:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4, 1)
                        else:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1, 1)
                    else:
                        if dx == dy == 1:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                min(cell.static + 1.4, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static), 1)
                        else:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                min(cell.static + 1, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static), 1)
                except IndexError:
                    pass

            if cell.get_X() - 1 > 0:
                for dx, dy in [(-1, 0), (-1, 1)]:
                    try:
                        if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                            if dy == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,
                                                                                                     1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1, 1)
                        else:
                            if dy == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                    min(cell.static + 1.4,
                                        cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static), 1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                    min(cell.static + 1, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),
                                    1)
                    except IndexError:
                        pass

            if cell.get_Y() - 1 > 0:
                for dx, dy in [(0, -1), (1, -1)]:
                    try:
                        if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                            if dx == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,
                                                                                                     1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1, 1)
                        else:
                            if dx == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                    min(cell.static + 1.4,
                                        cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static), 1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                    min(cell.static + 1, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),
                                    1)
                    except IndexError:
                        pass

    maximum = max(cell.static for line in cellular_space1 for cell in line)
    for line in cellular_space1:
        for cell in line:
            cell.static = round(maximum - cell.static, 1)

    for x, y in [(a, b) for a in range(1,3) for b in range(5, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(4, 8) for b in range(3, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(9, 12) for b in range(1, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(4, 8) for b in range(23, 25)]:
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
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4, 1)
                        else:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1, 1)
                    else:
                        if dx == dy == 1:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                min(cell.static + 1.4, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static), 1)
                        else:
                            cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                min(cell.static + 1, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static), 1)
                except IndexError:
                    pass

            if cell.get_X() - 1 > 0:
                for dx, dy in [(-1, 0), (-1, 1)]:
                    try:
                        if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                            if dy == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,
                                                                                                     1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1, 1)
                        else:
                            if dy == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                    min(cell.static + 1.4,
                                        cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static), 1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                    min(cell.static + 1, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),
                                    1)
                    except IndexError:
                        pass

            if cell.get_Y() - 1 > 0:
                for dx, dy in [(0, -1), (1, -1)]:
                    try:
                        if cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static == None:
                            if dx == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1.4,
                                                                                                     1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(cell.static + 1, 1)
                        else:
                            if dx == 1:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                    min(cell.static + 1.4,
                                        cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static), 1)
                            else:
                                cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static = round(
                                    min(cell.static + 1, cellular_space1[cell.get_Y() + dy][cell.get_X() + dx].static),
                                    1)
                    except IndexError:
                        pass

    for line in cellular_space1:
        for cell in line:
            cell.y = 25 - cell.y

    cellular_space1.reverse()

    maximum = max(cell.static for line in cellular_space1 for cell in line)
    for line in cellular_space1:
        for cell in line:
            cell.static = round(maximum - cell.static, 1)

    for x, y in [(a, b) for a in range(1,3) for b in range(5, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(4, 8) for b in range(3, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(9, 12) for b in range(1, 22, 2)]:
        cellular_space1[y][x].static = 0

    for x, y in [(a, b) for a in range(4, 8) for b in range(23, 25)]:
        cellular_space1[y][x].static = 0

    return cellular_space1


class Evacuee:  # define an Evacuee class
    def __init__(self, x, y, cellular_space1, cellular_space2, coe = 0.5):
        self.coe = coe
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate
        self.statics = [cellular_space1[self.y][self.x].static,
                        cellular_space2[self.y][self.x].static]  # strength of static floor field
        self.exit = False
        self.utility_distances = [0, 0]
        self.utility_crowd = [0, 0]
        self.utility_doors = [0, 0]
        self.probabilities = [e ** self.utility_doors[0] / (e ** self.utility_doors[0] + e ** self.utility_doors[1]),
                              e ** self.utility_doors[0] / (e ** self.utility_doors[0] + e ** self.utility_doors[1])]
        self.last_door = ''

    def get_X(self):  # get the x-coordinate
        return self.x

    def get_Y(self):  # get the y-coordinate
        return self.y

    def get_Static1(self):  # get the static field where the evacuee now stays
        return self.statics[0]

    def get_Static2(self):
        return self.statics[1]

    def move(self, dx, dy):  # movement into the next cell
        self.x += dx
        self.y += dy

    def update_statics(self, cellular_space1, cellular_space2):
        self.statics = [cellular_space1[self.y][self.x].static, cellular_space2[self.y][self.x].static]

    def update_utility_distances(self):
        self.utility_distances = [self.coe * self.statics[0] / sum(self.statics), self.coe * self.statics[1] / sum(self.statics)]

    def update_utility_doors(self):
        self.utility_doors = self.utility_distances + self.utility_crowd

    def update_probabilities(self):
        self.probabilities = [e ** self.utility_doors[0] / (e ** self.utility_doors[0] + e ** self.utility_doors[1]),
                              e ** self.utility_doors[0] / (e ** self.utility_doors[0] + e ** self.utility_doors[1])]

    def exit_judge(self, x_door, y_door):
        if self.get_X() == x_door and self.get_Y() == y_door:
            self.exit = True



class Space:
    def __init__(self, cellular_space1, cellular_space2):
        self.evacuees = []
        self.cellular_space1 = cellular_space1
        self.cellular_space2 = cellular_space2

    def create_evacuees(self, n, coefficient):
        number_evacuee = 0
        while number_evacuee < n:
            new = Evacuee(randrange(0, 12), randrange(0, 26), self.cellular_space1, self.cellular_space2, coe = coefficient)
            if new.statics[0] == 0 and new.statics[1] == 0 or new in self.evacuees:
                continue
            else:
                self.evacuees.append(new)
                number_evacuee += 1
        for evacuee in self.evacuees:
            evacuee.exit_judge(0, 0)
            evacuee.exit_judge(0, 25)

    def larger_static1(self, remain_evacuees):
        larger_static1 = []
        all_statics = [evacuee.get_Static1() for evacuee in remain_evacuees]
        for this_evacuee_static in all_statics:
            larger = [other_evacuee_static for other_evacuee_static in all_statics if
                      other_evacuee_static > this_evacuee_static]
            larger_static1.append(len(larger))
        return larger_static1

    def larger_static2(self, remain_evacuees):
        larger_static2 = []
        all_statics = [evacuee.get_Static2() for evacuee in remain_evacuees]
        for this_evacuee_static in all_statics:
            larger = [other_evacuee_static for other_evacuee_static in all_statics if
                      other_evacuee_static > this_evacuee_static]
            larger_static2.append(len(larger))
        return larger_static2

    def utility_crowd_assignment(self, larger_static1, larger_static2, remain_evacuees):
        for evacuee in remain_evacuees:
            if larger_static1[remain_evacuees.index(evacuee)] + larger_static2[remain_evacuees.index(evacuee)] != 0:
                evacuee.utility_crowd = [(1 - larger_static1[remain_evacuees.index(evacuee)] /
                                          (larger_static1[remain_evacuees.index(evacuee)] +
                                           larger_static2[remain_evacuees.index(evacuee)])) * (1-evacuee.coe),
                                         (1 - larger_static2[remain_evacuees.index(evacuee)] /
                                          (larger_static1[remain_evacuees.index(evacuee)] +
                                           larger_static2[remain_evacuees.index(evacuee)])) * (1-evacuee.coe)]
            else:
                evacuee.utility_crowd = [1, 1]

    def simulate(self, cellular_space1, cellular_space2,remain_evacuees,classroom):
        for evacuee in remain_evacuees:
            if random()<0.3:
                if random() < evacuee.probabilities[0]:
                    delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                    statics_around = []
                    delta_in_effect = []
                    for dx,dy in delta:
                        try:
                            if evacuee.get_X() + dx >= 0 and evacuee.get_Y() + dy >= 0:
                                statics_around.append(cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].static)
                                delta_in_effect.append((dx,dy))
                        except IndexError:
                            pass
                    for dx, dy in delta_in_effect:
                        try:
                            next_step_static = max(statics_around)
                            if cellular_space1[evacuee.get_Y() + dy][
                                evacuee.get_X() + dx].static == next_step_static and \
                                    cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].occupied == False:
                                if (evacuee.get_Y()+dy == 0 and evacuee.get_X()+dx == 0) or (evacuee.get_Y()+dy == 25 and evacuee.get_X()+dx == 0):
                                    cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                else:
                                    cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                    cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                classroom.undraw_evacuees(evacuee)
                                evacuee.move(dx, dy)
                                # if not (evacuee.get_X() == 0 and evacuee.get_Y() == 0) and (
                                #         evacuee.get_X() == 0 and evacuee.get_Y() == 25):
                                classroom.draw_evacuee(evacuee)
                                break
                        except IndexError:
                            pass
                    evacuee.exit_judge(0, 0)
                    evacuee.exit_judge(0, 25)
                    evacuee.last_door = 'door 1'
                else:
                    delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                    statics_around = []
                    delta_in_effect = []
                    for dx, dy in delta:
                        try:
                            if evacuee.get_X() + dx >= 0 and evacuee.get_Y() + dy >= 0:
                                statics_around.append(cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].static)
                                delta_in_effect.append((dx,dy))
                        except IndexError:
                            pass
                    for dx, dy in delta_in_effect:
                        try:
                            # statics_around.append(cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].static)
                            next_step_static = max(statics_around)
                            if cellular_space2[evacuee.get_Y() + dy][
                                evacuee.get_X() + dx].static == next_step_static and \
                                    cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].occupied == False:
                                if (evacuee.get_Y()+dy == 0 and evacuee.get_X()+dx == 0) or (evacuee.get_Y()+dy == 25 and evacuee.get_X()+dx == 0):
                                    cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                else:
                                    cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                    cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                classroom.undraw_evacuees(evacuee)
                                evacuee.move(dx, dy)
                                # if not (evacuee.get_X() == 0 and evacuee.get_Y() == 0) and (
                                #         evacuee.get_X() == 0 and evacuee.get_Y() == 25):
                                classroom.draw_evacuee(evacuee)
                                break
                        except IndexError:
                            pass
                    evacuee.exit_judge(0, 0)
                    evacuee.exit_judge(0, 25)
                    evacuee.last_door = 'door 2'
            else:
                if evacuee.last_door == 'door 1':
                    delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                    statics_around = []
                    delta_in_effect = []
                    for dx, dy in delta:
                        try:
                            if evacuee.get_X() + dx >= 0 and evacuee.get_Y() + dy >= 0:
                                statics_around.append(
                                    cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].static)
                                delta_in_effect.append((dx, dy))
                        except IndexError:
                            pass
                    for dx, dy in delta_in_effect:
                        try:
                            next_step_static = max(statics_around)
                            if cellular_space1[evacuee.get_Y() + dy][
                                evacuee.get_X() + dx].static == next_step_static and \
                                    cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].occupied == False:
                                if (evacuee.get_Y() + dy == 0 and evacuee.get_X() + dx == 0) or (
                                        evacuee.get_Y() + dy == 25 and evacuee.get_X() + dx == 0):
                                    cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                else:
                                    cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                    cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                classroom.undraw_evacuees(evacuee)
                                evacuee.move(dx, dy)
                                # if not (evacuee.get_X() == 0 and evacuee.get_Y() == 0) and (
                                #         evacuee.get_X() == 0 and evacuee.get_Y() == 25):
                                classroom.draw_evacuee(evacuee)
                                break
                        except IndexError:
                            pass
                    evacuee.exit_judge(0, 0)
                    evacuee.exit_judge(0, 25)
                else:
                    delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                    statics_around = []
                    delta_in_effect = []
                    for dx, dy in delta:
                        try:
                            if evacuee.get_X() + dx >= 0 and evacuee.get_Y() + dy >= 0:
                                statics_around.append(
                                    cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].static)
                                delta_in_effect.append((dx, dy))
                        except IndexError:
                            pass
                    for dx, dy in delta_in_effect:
                        try:
                            next_step_static = max(statics_around)
                            if cellular_space2[evacuee.get_Y() + dy][
                                evacuee.get_X() + dx].static == next_step_static and \
                                    cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].occupied == False:
                                if (evacuee.get_Y() + dy == 0 and evacuee.get_X() + dx == 0) or (
                                        evacuee.get_Y() + dy == 25 and evacuee.get_X() + dx == 0):
                                    cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                else:
                                    cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                    cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                    cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                classroom.undraw_evacuees(evacuee)
                                evacuee.move(dx, dy)
                                # if not (evacuee.get_X() == 0 and evacuee.get_Y() == 0) and (
                                #         evacuee.get_X() == 0 and evacuee.get_Y() == 25):
                                classroom.draw_evacuee(evacuee)
                                break
                        except IndexError:
                            pass
                    evacuee.exit_judge(0, 0)
                    evacuee.exit_judge(0, 25)
            # classroom.win.flush()
        update(1)


    def simulate_once(self,cellular_space1, cellular_space2,remain_evacuees,classroom):
        for evacuee in remain_evacuees:
            if random() < evacuee.probabilities[0]:
                delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                statics_around = []
                delta_in_effect = []
                for dx, dy in delta:
                    try:
                        if evacuee.get_X() + dx >= 0 and evacuee.get_Y() + dy >= 0:
                            statics_around.append(cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].static)
                            delta_in_effect.append((dx, dy))
                    except IndexError:
                        pass
                for dx, dy in delta_in_effect:
                    try:
                        next_step_static = max(statics_around)
                        if cellular_space1[evacuee.get_Y() + dy][
                            evacuee.get_X() + dx].static == next_step_static and \
                                cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].occupied == False:
                            if (evacuee.get_Y() + dy == 0 and evacuee.get_X() + dx == 0) or (
                                    evacuee.get_Y() + dy == 25 and evacuee.get_X() + dx == 0):
                                cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                            else:
                                cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                            classroom.undraw_evacuees(evacuee)
                            evacuee.move(dx, dy)
                            # if not (evacuee.get_X()==0 and evacuee.get_Y() == 0) and (
                            #         evacuee.get_X()==0 and evacuee.get_Y()==25):
                            classroom.draw_evacuee(evacuee)
                    except IndexError:
                        pass
                evacuee.exit_judge(0, 0)
                evacuee.exit_judge(0, 25)
                evacuee.last_door = 'door 1'
            else:
                delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                statics_around = []
                delta_in_effect = []
                for dx, dy in delta:
                    try:
                        if evacuee.get_X() + dx >= 0 and evacuee.get_Y() + dy >= 0:
                            statics_around.append(cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].static)
                            delta_in_effect.append((dx, dy))
                    except IndexError:
                        pass
                for dx, dy in delta_in_effect:
                    try:
                        next_step_static = max(statics_around)
                        if cellular_space2[evacuee.get_Y() + dy][
                            evacuee.get_X() + dx].static == next_step_static and \
                                cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].occupied == False:
                            if (evacuee.get_Y() + dy == 0 and evacuee.get_X() + dx == 0) or (
                                    evacuee.get_Y() + dy == 25 and evacuee.get_X() + dx == 0):
                                cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                            else:
                                cellular_space1[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                cellular_space1[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                                cellular_space2[evacuee.get_Y()][evacuee.get_X()].not_occupied()
                                cellular_space2[evacuee.get_Y() + dy][evacuee.get_X() + dx].is_occupied()
                            classroom.undraw_evacuees(evacuee)
                            evacuee.move(dx, dy)
                            # if not (evacuee.get_X() == 0 and evacuee.get_Y() == 0) and (
                            #         evacuee.get_X() == 0 and evacuee.get_Y() == 25):
                            classroom.draw_evacuee(evacuee)
                    except IndexError:
                        pass
                evacuee.exit_judge(0, 0)
                evacuee.exit_judge(0, 25)
                evacuee.last_door = 'door 2'
            # classroom.win.flush()
        update(1)


inputwindow = InputDialog(0,0.0)
interaction = inputwindow.interact()
if interaction == 'Simulate!':
    people, coefficient = inputwindow.getValues()
    inputwindow.close()

    classroom105 = Classroom()
    classroom105.draw_cell_horizontal_line()
    classroom105.draw_cell_vertical_line()
    classroom105.fill_green()
    classroom105.draw_doors()

    cellular_space1 = create_space1()
    cellular_space2 = create_space2()

    classroom = Space(cellular_space1, cellular_space2)
    classroom.create_evacuees(people, coefficient)
    remained_evacuees = [evacuee for evacuee in classroom.evacuees if evacuee.exit == False]
    time_steps = 0
    # print([[evacuee.get_X(),evacuee.get_Y()] for evacuee in remained_evacuees])
    for evacuee in remained_evacuees:
        classroom105.draw_evacuee(evacuee)
        cellular_space1[evacuee.get_Y()][evacuee.get_X()].is_occupied()
        cellular_space2[evacuee.get_Y()][evacuee.get_X()].is_occupied()
        evacuee.update_statics(cellular_space1, cellular_space2)
        evacuee.update_utility_distances()
        classroom.utility_crowd_assignment(larger_static1=classroom.larger_static1(remained_evacuees),
                                           larger_static2=classroom.larger_static2(remained_evacuees),
                                           remain_evacuees=remained_evacuees)
        evacuee.update_utility_doors()
        evacuee.update_probabilities()
    classroom.simulate_once(cellular_space1, cellular_space2, remained_evacuees, classroom105)
    # print([[evacuee.get_X(), evacuee.get_Y()] for evacuee in remained_evacuees])
    remained_evacuees = [evacuee for evacuee in remained_evacuees if evacuee.exit == False]
    while remained_evacuees:
        time_steps += 1
        for evacuee in remained_evacuees:
            cellular_space1[evacuee.get_Y()][evacuee.get_X()].is_occupied()
            cellular_space2[evacuee.get_Y()][evacuee.get_X()].is_occupied()
            evacuee.update_statics(cellular_space1, cellular_space2)
            evacuee.update_utility_distances()
            classroom.utility_crowd_assignment(larger_static1=classroom.larger_static1(remained_evacuees),
                                               larger_static2=classroom.larger_static2(remained_evacuees),
                                               remain_evacuees=remained_evacuees)
            evacuee.update_utility_doors()
            evacuee.update_probabilities()
        classroom.simulate(cellular_space1, cellular_space2, remained_evacuees, classroom105)
        # print([[evacuee.get_X(), evacuee.get_Y()] for evacuee in remained_evacuees])
        remained_evacuees = [evacuee for evacuee in remained_evacuees if evacuee.exit == False]
    print(time_steps)

    a = input('')
    classroom105.win.close()
else:
    inputwindow.close()

# clas