#!/usr/bin/python3
"""This module has a class Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square class that inherits from the Rectangle class"""

    def __init__(self, size):
        """initializes width and height"""

        self.__size = size
        super().__init__(size, size)
