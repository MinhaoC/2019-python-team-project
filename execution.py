classroom105 = Classroom()
classroom105.draw_cell_horizontal_line()
classroom105.draw_cell_vertical_line()
classroom105.fill_green()
classroom105.draw_doors()

cellular_space1 = create_space1()
cellular_space2 = create_space2()
classroom = Space(cellular_space1, cellular_space2)
classroom.create_evacuees(30)
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
classroom.simulate_once(cellular_space1, cellular_space2, remained_evacuees,classroom105)
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
    classroom.simulate(cellular_space1, cellular_space2, remained_evacuees,classroom105)
    # print([[evacuee.get_X(), evacuee.get_Y()] for evacuee in remained_evacuees])
    remained_evacuees = [evacuee for evacuee in remained_evacuees if evacuee.exit == False]
print(time_steps)

a = input('')
classroom105.win.close()