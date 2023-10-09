#!/usr/bin/python3
"""This module has only one function
The function returns the list of available attributes and methods
of an object"""


def lookup(obj):
    """Returns all the methods and attributes of an object

    Args
        obj (object): object to be checked for methods and attributes

    Returns:
        list: containing all the method and attribute names
    """

    return dir(obj)
