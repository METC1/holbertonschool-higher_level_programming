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

    def integer_validator(self, name, value):
        """
        Public method validates if number is an integer
        """

        if type(value) is not  int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
