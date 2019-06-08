from graphics import *
from Button import *
class InputDialog:
    def __init__(self,number,weigh):
        self.win = win = GraphWin('Evacuee Number', 200, 300)
        win.setCoords(0,4.5,4,.5)

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



