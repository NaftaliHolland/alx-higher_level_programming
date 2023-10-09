#!/usr/bin/python3
"""This module has a class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangele class that inherits from the BaseGeometry class"""

    def __init__(self, width, height):
        """initializes width and height"""

        self.__width = width
        self.__height = height

        if super().integer_validator("width", width):
            self.__width = width

        if super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns an string representation of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
