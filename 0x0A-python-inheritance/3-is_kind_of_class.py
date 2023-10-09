#!/usr/bin/python3
"""Contains one function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class
    or a class that inherits a_class"""

    return isinstance(obj, a_class)
