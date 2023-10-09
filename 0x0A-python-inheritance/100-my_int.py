#!/usr/bin/python3
"""This module contains a rebel class MyInt"""


class MyInt(int):
    """inherits the int class and overidest the __eq__() and __ne__() methods"""

    def __eq__(self, other):
        """overides the default equals method"""
        
        return not(super().__eq__(other))

    def __ne__(self, other):
        """overides the inbuilt not equals to method"""

        return super().__eq__(other)
