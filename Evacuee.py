# This module defines a new class Evacuee
# Contributor: cmh
# 2019/05/14

class Evacuee:            # define an Evacuee class
    def __init__(self, x, y, static):
        self.x = x             # x-coordinate
        self.y = y             # y-coordinate
        self.static = static    # strength of static floor field
        self.exit = False

    def get_X(self):            # get the x-coordinate
        return self.x

    def get_Y(self):            # get the y-coordinate
        return self.y

    def get_Static(self):       # get the static field where the evacuee now stays
        return self.static

    def move(self, dx, dy):     # movement into the next cell
        self.x += dx
        self.y += dy

    def exit(self, x_door, y_door):
        if self.get_X() == x_door and self.get_Y() == y_door:
            self.exit = True
