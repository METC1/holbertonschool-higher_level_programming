#!/usr/bin/python3
"""
Checks if object is an instance of the class provided
or an instance of a class inherited
"""


def is_kind_of_class(obj, a_class):
    """
    method, checks if obj is an instance of a_class or
    if it is inherited from a_class, true if it is, false
    otherwise
    """

    return isinstance(obj, a_class)
