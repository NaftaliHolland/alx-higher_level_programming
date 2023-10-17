#!/usr/bin/python3
"""This module contains a Rectangle class that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """A simple rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the Rectangle instance"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def __width(self):
        """width getter"""
        return self.__width

    @__width.setter
    def __width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def __height(self):
        """height getter"""
        return self.__height

    @__height.setter
    def __height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def __x(self):
        """x getter"""
        return self.__x

    @__x.setter
    def __x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def __y(self):
        """y getter"""
        return self.__y

    @__y.setter
    def __y(self, value):
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
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) == 5:
            self.__y = args[4]
