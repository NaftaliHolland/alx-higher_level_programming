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
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
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
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
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
