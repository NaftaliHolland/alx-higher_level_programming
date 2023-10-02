#!/usr/bin/python3
"""This is a class representation of a rectangle

Has private attributes width and height
"""


class Rectangle:
    """This is a class representation of a rectangle

    This class has the attributes of a rectangle

    width (int): width of the rectangle
    height (int): height of the rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes size after checking
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the rectangle

        Returns: the private instance variable width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the recatangle

        Checks to ensure that value is an integer that is greter than or
        equal to zero

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retirieves the height of the rectangle

        Returns: returns the private instance variable height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle

        Checks to ensure that value is an integer that is greater than or
        equal to zero
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of the rectangle

        Returns: the area of the rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle

        Returns: the pereimeter of the rectangle
        """
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rectangle with the character #

        Returns: a string representation of the character
        """
        my_string = ""

        for i in range(self.__height):
            for j in range(self.__width):
                my_string += "#"
            my_string += "\n"

        my_string = my_string.rstrip("\n")
        return my_string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints something when an object is deleted
        """
        global number_of_instances
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
