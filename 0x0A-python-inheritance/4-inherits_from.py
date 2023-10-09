#!/usr/bin/python3
"""This module has only one function inherits_from"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherits a_class
    directly or indirectly"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
