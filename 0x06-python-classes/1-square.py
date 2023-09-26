#!/usr/bin/python3
"""This module defines a Square class

Has only the definition for now

"""


class Square:
    """
    a class that defines a square

    """
    def __init__(self, size):
        """
        initialization method

        this method is used to instantiate this classe's attributes

        Args:
            size: a private attribute representing the size of the square
        """
        self.__size = size
