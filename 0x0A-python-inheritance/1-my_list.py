#!/usr/bin/python3
"""This module has a class that inherits the builtin list class"""

class MyList(list):
    """This class inherits the list class and has
    one method"""

    def print_sorted(self):
        """Prints the list values in a sorted manner"""
        print(sorted(self))
