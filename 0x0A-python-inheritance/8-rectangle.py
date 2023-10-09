#!/usr/bin/python3
"""This module has a class Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    """A rectangele class that inherits from the BaseGeometry class"""

    def __init__(self, width, height):
        """initializes width and height"""

        if super().integer_validator("width", width):
            self.__width = width

        if super().integer_validator("height", height):
            self.__height = height
