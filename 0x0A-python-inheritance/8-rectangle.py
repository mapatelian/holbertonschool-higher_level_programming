#!/usr/bin/python3
"""Module that initializes a new class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__height = height
        self.__width = width
