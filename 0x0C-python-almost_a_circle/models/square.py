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

    def update(self, *args, **kwargs):
        """updates the attribute"""
        if args is not None and len(args) >= 1:
            attributes = ["id", "width", "height", "x", "y"]

            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """retuns the dictionary representation of a Square"""

        return {
                "id": self.x,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
