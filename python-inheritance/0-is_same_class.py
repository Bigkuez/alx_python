#!/usr/bin/python3
"""a function that returns True
or False if the object is exactly an instance oft the
specified class.
"""


def is_same_class(obj, a_class):
    """ a function that returns True if the object is exactly an instance of the specified class 
    """
    return type(obj) is a_class
