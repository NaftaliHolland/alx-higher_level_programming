#!/usr/bin/python3
"""This file contatins one functiion"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""

    result, result_row = list(), list()

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or not all(len(i) > 0 for i in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or not all(len(i) > 0 for i in m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(i, (int, float)) for j in m_a for i in j):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(i, (int, float)) for j in m_b for i in j):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[0]) == len(j) for j in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(m_b[0]) == len(j) for j in m_b):
        raise TypeError("each row of m_b must be of the same size")

    columns, rows = len(m_a[0]), len(m_b)

    if rows != columns:
        raise ValueError("m_a and m_b can't be multiplied")
    result = list([0 for i in range(columns)] for k in range(len(m_a)))

    for i in range(len(m_a)):
        for k in range(rows):
            for j in range(rows):
                result[i][k] += m_a[i][j] * m_b[j][k]

    return result
