#!/usr/bin/python3
"""
Class Rectangle, inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle initialization
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Area calculation of Rectangle
        """
        self.area = self.width * self.height
        return self.area

    def display(self):
        """
        Display the rectangle representation by plotting
        the # character
        """
        for line in range(self.y):
            print("")
        for line2 in range(self.height):
            for column in range(self.x):
                print(" ", end='')
            for column2 in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        else:
            if width <= 0:
                raise ValueError("Width must be > 0")
            else:
                self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
