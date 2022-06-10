#!/usr/bin/python3
"""
Class first create
"""


class Base:
    """
    Class Base manages the id attribute in all future classes
    and avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id