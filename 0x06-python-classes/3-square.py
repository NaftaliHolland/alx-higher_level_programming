#!/usr/bin/python3
"""This module defines a Square class

The class will have some properties

"""


class Square:
    """A class that defines a square

    Args:
    No public arguments yet

    """
    def __init__(self, size=0):
        """Initializes size after checking some conditions.

        This method ensures that size is an integer and is not less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of a square

        Returns: the area of the squre
        """
        return self.__size ** 2
