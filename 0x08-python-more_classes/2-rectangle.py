#!/usr/bin/python3
class Rectangle:
    """New class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialisation of parameters

        Arguments:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Retrieving height
        """
        return self.height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Retrieving width
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

    def area(self):
        """Method that computes the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Method that computes the perimeter of the rectangular
        """
        check = 1
        if self.__height == 0 or self.__width == 0:
            check = 0
        return (self.__height + self.__width) * 2 * check
