from math import e
class Evacuee:  # define an Evacuee class
    def __init__(self, x, y, cellular_space1, cellular_space2):
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
        self.utility_distances = [0.9 * self.statics[0] / sum(self.statics), 0.9 * self.statics[1] / sum(self.statics)]

    def update_utility_doors(self):
        self.utility_doors = self.utility_distances + self.utility_crowd

    def update_probabilities(self):
        self.probabilities = [e ** self.utility_doors[0] / (e ** self.utility_doors[0] + e ** self.utility_doors[1]),
                              e ** self.utility_doors[0] / (e ** self.utility_doors[0] + e ** self.utility_doors[1])]

    def exit_judge(self, x_door, y_door):
        if self.get_X() == x_door and self.get_Y() == y_door:
            self.exit = True