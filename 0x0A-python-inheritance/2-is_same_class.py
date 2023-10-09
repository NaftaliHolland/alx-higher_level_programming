#!/usr/bin/python3
"""This module has only one function is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class false otherwise"""

    return type(obj) is a_class
