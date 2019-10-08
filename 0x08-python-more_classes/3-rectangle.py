#!/usr/bin/python3
class Rectangle:
    """Class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Retrives value of height
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
        """Retrieves the value of width
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
        """Computes area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Computes a perimeter of the rectangle
        """
        check = 2
        if self.__width == 0 or self.__height == 0:
            check = 0
        return (self.__height + self.__width) * check

    def __str__(self):
        """String representation of the rectangle
        """
        str = ""
        for i in range(self.__height):
            for k in range(self.__width):
                str = str + '#'
            if i != self.__height - 1:
                str = str + '\n'
        return str
