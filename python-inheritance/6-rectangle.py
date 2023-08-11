#!/usr/bin/python3
"""
    Represents a BaseGeometry.
"""
class BaseGeometry:
    # ... (previous implementation of BaseGeometry)

    def area(self):
        """
        Calculate the area of the geometry.

        This method is not implemented in the base class and should be overridden
        in the derived classes.

        Raises:
            Exception: Indicates that the method is not implemented.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer and greater than 0.

        Args:
            name (str): The name of the value, used in the error message.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        None (inherits the methods from BaseGeometry).

    Example:
        r = Rectangle(3, 5)
        print(r)
    """
    def __init__(self, width, height):
        """
        Initialize the Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
