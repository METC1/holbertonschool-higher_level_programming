#!/usr/bin/python3
"""
Returns the dictionary description
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description
    with simple data structure(list, dictionary, string,
    integer, and boolean) for JSON serialization of an
    Object
    """
    return obj.__dict__
