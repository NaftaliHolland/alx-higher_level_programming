#!/usr/bin/python3
""" This module has a function that tries to add an attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """ Adds attribute to an object """

    if not hasattr(obj, attr_name):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
