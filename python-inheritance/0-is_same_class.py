#!/usr/bin/python3
"""
    Represents a is_same_class.
"""
def is_same_class(obj, a_class):
    """
    Check if the given object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise False.

    Example:
        a = 1
        is_same_class(a, int)  # Returns True
        is_same_class(a, float)  # Returns False
        is_same_class(a, object)  # Returns False
    """
    return type(obj) is a_class
