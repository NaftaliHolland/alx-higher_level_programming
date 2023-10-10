#!/usr/bin/python3
"""Module documentation"""
import json


def from_json_string(my_str):
    """returns a python object represented by a json string"""

    return json.loads(my_str)
