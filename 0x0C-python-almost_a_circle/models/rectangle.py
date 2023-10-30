#!/usr/bin/python3
"""This module contains a Rectangle class that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """A simple rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the Rectangle instance"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of a rectangle

        Returns: area
        """
        return self.__width * self.__height

    def display(self):
        """prints to stdout the Rectangle instance"""

        for i in range(self.__height):
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overiding the __str__() method to return some useful infomation
        about the Rectangle instance"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) >= 1:
            attributes = ["id", "width", "height", "x", "y"]

            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the object"""
        return {
                "x": self.__x,
                "y": self.__y,
                "height": self.__height,
                "width": self.__width
                }
