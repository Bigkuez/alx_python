#!/usr/bin/python3
"""
A function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Check if the given object is an instance of a class that inherited (directly or indirectly)
    from the specified class.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
