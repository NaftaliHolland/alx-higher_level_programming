#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    neumerator, denominator = 0, 0
    for tup in my_list:
        neumerator += tup[0] * tup[1]
        denominator += tup[1]

    return neumerator / denominator
