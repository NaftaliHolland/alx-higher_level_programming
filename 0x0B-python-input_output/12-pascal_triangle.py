#!/usr/bin/python3
"""Module documentation"""


def pascal_triangle(n):
    """creates the pascal's triangle

    Returns: A list of lists of integers representating the
            pascal's tringle
    """

    pascal = list()
    if n <= 0:
        return pascal

    for i in range(n):
        inner_list = list()
        for j in range(i + 1):
            if j == 0 or j == i:
                inner_list.append(1)
            else:
                inner_list.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(inner_list)
    return pascal
