#!/usr/bin/python3
"""
Function, returns true if the object is an instance of a class specified
false if otherwise
"""


def is_same_class(obj, a_class):
    """
    method, returns true if the object specified is exactly an instance of the specified class. otherwise return false.
    """

    if isinstance(obj, a_class):
        return True
    return False
