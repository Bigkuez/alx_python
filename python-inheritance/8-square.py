#!/usr/bin/python3
"""
Module contains the definition of class Square that inherits from Rectangle.
"""

Rectangle = __import__('7-rectangle').Rectangle  # Import Rectangle class
integer_validator = __import__('7-base_geometry').integer_validator  # Import integer_validator function

class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square shape.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.

        Raises:
            ValueError: If size is not a positive integer.
        """
        integer_validator("size", size)  # Validate size as a positive integer
        super().__init__(size, size)  # Call the constructor of the base class with width and height as size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__width * self.__height  # In a square, width and height are the same
