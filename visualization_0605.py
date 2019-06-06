from graphics import *

class Classroom:
    def __init__(self):
        self.evacuees_pos = []
        self.win = GraphWin('Classroom 105', 320, 520)
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