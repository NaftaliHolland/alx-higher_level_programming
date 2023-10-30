#!/usr/bin/python3
"""This file has one function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Uses numpy to multiply a matrix"""

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

    return np.matmul(m_a, m_b)
