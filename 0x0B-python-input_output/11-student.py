#!/usr/bin/python3
"""Module documentation"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """initializes the instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
        for attributes specified in attrs
        """

        if attrs:
            new_dict = dict()
            for attr in attrs:
                if attr not in self.__dict__.keys():
                    continue
                new_dict[attr] = self.__dict__[attr]

            if len(new_dict) > 0:
                return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all the attributes of the Student instance"""

        self.__dict__ = json
