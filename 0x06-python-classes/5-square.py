#!/usr/bin/python3
"""This module defines a Square class

The class will have some properties

"""


class Square:
    """A class that defines a square

    Args:
    No public arguments yet

    """
    def __init__(self, size=0):
        """Initializes size after checking some conditions.

        This method ensures that size is an integer and is not less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of a square

        Returns: the area of the squre
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves a private instance variable size

        Returns: the private instande variable size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of an instance variable size

        Checks to ensure value being passed to __size is valid

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints in stdout the square with #
        """
        if self.size > 0:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
        print()
