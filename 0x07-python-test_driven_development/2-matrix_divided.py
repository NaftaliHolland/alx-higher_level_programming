#!/usr/bin/python3
"""Module documentation"""


def matrix_divided(matrix, div):
    """Divides a matrix"""

    if not all(
                isinstance(j, (int, float))
                for i in matrix for j in i):
        raise TypeError(
                         """matrix must be a matrix
                         (list of lists)of integers/floats
                         """)

    if not all(
                x == [len(i) for i in matrix][0]
                for x in [len(i)
                          for i in matrix]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(k/div, 2) for k in j] for j in matrix]
