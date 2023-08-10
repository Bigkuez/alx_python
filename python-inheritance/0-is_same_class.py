#!/usr/bin/python3
"""Module consists of a function that returns True
or False if the object is exactly an instance oft the
specified class.
"""


def is_same_class(obj, a_class):
    """Function that returns True or False if the object is
    exactly an instance of the specified class.
    """
    return type(obj) is a_class
