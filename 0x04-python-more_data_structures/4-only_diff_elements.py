#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = []
    my_set = set()

    my_list.extend(set_1)
    my_list.extend(set_2)

    for i in my_list:
        if my_list.count(i) == 1:
            my_set.add(i)

    return my_set
