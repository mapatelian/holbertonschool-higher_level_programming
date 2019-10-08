#!/usr/bin/python3
class Rectangle:
    """New class Rectangle that defines a a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Iniotialization of the arguments
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @property
    def height(self):
        """Retrieving the height
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

    def area(self):
        """Module that computes the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Module to compute a perimeter of the rectangle
        """
        check = 2
        if self.__height == 0 or self.__width == 0:
            check = 0
        return (self.__height + self.__width) * check

    def __str__(self):
        """String representation of the rectangle
        """
        str = ""
        for i in range(self.__height):
            for k in range(self.__width):
                str = str + "#"
            if i != self.__height - 1:
                str = str + '\n'
        return str

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deleting an instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
