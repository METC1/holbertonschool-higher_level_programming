#!/usr/bin/python3
"""
BaseGeometry with exception
raises exception on method not implemented
"""


class BaseGeometry:
    """
    Class BaseGeometry area implementing
    """

    def area(self):
        """
        Raises exception because method is not implemented
        """

        raise Exception("area() is not implemented")
