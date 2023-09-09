#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_1, list_2 = list(tuple_a), list(tuple_b)

    while len(list_1) < 2:
        list_1.append(0)

    while len(list_2) < 2:
        list_2.append(0)

    new_tuple = (list_1[0] + list_2[0]), (list_1[1] + list_2[1])

    return new_tuple
