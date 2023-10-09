#!/usr/bin/python3
"""This module has a class Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square class that inherits from the Rectangle class"""

    def __init__(self, size):
        """initializes width and height"""

        self.__size = size
        if super().integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returns the string representation of a square"""
        return "[square] {}/{}".format(self.__size, self.__size)
