#!/usr/bin/python3
"""square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        self.__width = value
        self.__height = value

    def __str__(self):
        """overiding the string method"""

        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )

    def to_dictionary(self):
        """retuns the dictionary representation of a Square"""

        return {
                "id": self.x,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
