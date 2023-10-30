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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation to a file"""

        my_list = list()
        string = "[]"
        with open("{}.json".format(
                cls.__name__),
                mode="w",
                encoding="utf-8"
        ) as f:
            if list_objs is not None:
                for i in range(len(list_objs)):
                    my_list.append(list_objs[i].to_dictionary())
                string = cls.to_json_string(my_list)

            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation of json_string"""

        if json_string is None:
            return list()

        return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set"""
        dummy = cls(5, 2, 2)
        dummy.update(dictionary)
        return dummy
