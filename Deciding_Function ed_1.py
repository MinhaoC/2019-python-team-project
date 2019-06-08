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
                    evacuee.exit_judge(0, 0)
                    evacuee.exit_judge(0, 25)
                    # classroom.win.flush()
        update(1)