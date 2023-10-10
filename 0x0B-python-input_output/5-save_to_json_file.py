#!/usr/bin/python3
"""module documentation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object in json format to a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
