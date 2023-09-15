#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for _ in matrix:
        new_list.append(list(map(lambda x: x ** 2, _)))

    return new_list
