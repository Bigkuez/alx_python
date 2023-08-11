#!/usr/bin/python3
"""Module consists of a Rectangle class that
inherits from BaseGeometry.
"""
BaseGeometry = __import__('5-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Initializing the class."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Method that returns the area of the instance. """
        return self.__width * self.__height

    def __str__(self):
        """Special method that returns the printable string. """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
    