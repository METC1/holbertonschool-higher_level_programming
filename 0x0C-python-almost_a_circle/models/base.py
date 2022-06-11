#!/usr/bin/python3
"""
Class first create
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON representation of list_objs to a file
        """
        if list_objs is None or list_objs == []:
            listo = []
        else:
            listo = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__+".json", "w") as f:
            f.write(cls.to_json_string(listo))
