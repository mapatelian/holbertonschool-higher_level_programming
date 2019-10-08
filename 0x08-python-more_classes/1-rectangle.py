#!/usr/bin/python3
class Rectangle:
    """Class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialisation arguments

        Arguments:
        width (int): width of the rectangle
        height(int): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving width.
        """
        return self.width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrievibg height
        """
        return self.height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__heght = value
