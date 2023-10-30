#!/usr/bin/python3
""" This module has a function that tries to add an attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """ Adds attribute to an object """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
