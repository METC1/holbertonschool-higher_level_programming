#!/usr/bin/python3
"""
Checks if object is an instance of the class provided
or inherited directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    method, checks if obj is an instance of a_class that
    inherited from a_class, directly or indirectly,
    true if it is, false  otherwise
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
