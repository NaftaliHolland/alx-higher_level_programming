#!/usr/bin/python3
"""square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the attributes"""
        super().__init__(size, size, x, y, id)

        def __str__(self):
            """overiding the string method"""
            return """
                [Square] ({}) {}/{} - {}
                """.format(self.id, self.__x, self.__y, self.__width)
