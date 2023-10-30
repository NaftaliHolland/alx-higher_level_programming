#!/usr/bin/python3
"""This is the base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"

        return json.dumps(list_dictionaries)
