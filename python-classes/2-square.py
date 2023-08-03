#!/usr/bin/python3
"""
    Represents a square.
"""
class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
