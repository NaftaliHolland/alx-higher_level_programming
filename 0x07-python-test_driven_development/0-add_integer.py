#!/usr/bin/python3
"""This module contains a function that adds 2 integers"""


def add_integer(a, b=98):
    """adds two integers

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b
