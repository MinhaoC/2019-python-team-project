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


classroom105 = Classroom()
classroom105.draw_cell_horizontal_line()
classroom105.draw_cell_vertical_line()
classroom105.fill_green()
classroom105.draw_doors()
a = input('')
classroom105.win.close()