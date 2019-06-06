from Evacuee import *
from random import randrange,random
from graphics import *
class Space:
    def __init__(self, cellular_space1, cellular_space2):
        self.evacuees = []
        self.cellular_space1 = cellular_space1
        self.cellular_space2 = cellular_space2

    def create_evacuees(self, n):
        number_evacuee = 0
        while number_evacuee < n:
            new = Evacuee(randrange(0, 12), randrange(0, 26), self.cellular_space1, self.cellular_space2)
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
                                           larger_static2[remain_evacuees.index(evacuee)])) * 0.1,
                                         (1 - larger_static2[remain_evacuees.index(evacuee)] /
                                          (larger_static1[remain_evacuees.index(evacuee)] +
                                           larger_static2[remain_evacuees.index(evacuee)])) * 0.1]
            else:
                evacuee.utility_crowd = [1, 1]