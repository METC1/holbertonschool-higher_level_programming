#!/usr/bin/python3
"""
Searches attributes and methods of an object
"""

def lookup(obj):
    """
    Function that returns list of available attributes and methods of an object"""
    return [method_name for method_name in dir(obj)]
