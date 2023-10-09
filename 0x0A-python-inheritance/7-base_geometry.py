#!/usr/bin/python3
"""This module has a class BaseGeometry that defines geometrical shapes"""


class BaseGeometry:
    """Has an instance method area()"""

    def area(self):
        """Raise:
                area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
