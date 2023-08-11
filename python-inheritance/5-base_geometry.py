#!/usr/bin/python3
"""
    Module represents a BaseGeometry.
"""
class BaseGeometry:
    """
    A base class for geometry-related operations.

    
    """
    def area(self):
        """
        Calculate the area of the geometry.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer and greater than 0.

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
