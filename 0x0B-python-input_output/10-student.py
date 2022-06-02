#!/usr/bin/python3
"""
Class that defines a student
"""


class Student:
    """
    student class with first name, last name, age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            attrs_collect = {}
            for attrib in attrs:
                for key, value in self.__dict__.items():
                    if key == attrib:
                        attrs_collect[key] = value
            return attrs_collect
        else:
            return (self.__dict__)
