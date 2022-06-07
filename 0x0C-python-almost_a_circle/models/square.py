#!/usr/bin/python3
"""
Class Square, inherits from Rectangle
"""


Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square initialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, super().x, super().y, super().width)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute of Square
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("Width must be an integer")
        else:
            if size <= 0:
                raise ValueError("Width must be > 0")
            else:
                self.width = size
                self.height = size
