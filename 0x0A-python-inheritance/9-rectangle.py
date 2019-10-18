#!/usr/bin/python3
"""Module that initializes a new class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from class BaseGeometry
    """

    def __init__(self, width, height):
        """Instantiation private width and height
        and calls to super to access method of the base class
        """
        super().integer_validator('height', height)
        super().integer_validator('width', width)
        self.__height = height
        self.__width = width

    def area(self):
        """Method to compute area
        """
        return self.__height * self.__width

    def __str__(self):
        """string method
        """
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
