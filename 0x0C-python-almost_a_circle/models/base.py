#!/usr/bin/python3
"""This is the base module"""


class Base:
    """This is the base of all other classes in this and other modules"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the id"""

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
