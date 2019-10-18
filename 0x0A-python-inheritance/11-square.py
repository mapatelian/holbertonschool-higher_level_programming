#!/usr/bin/python3
"""Module that initializes a new class
"""


Rectangle = __import__('9-rectangle').Rectangle
Square = __import__('10-square').Square


class Square(Rectangle):
    """New class Square that inherits from class Rectangle
    """
    def __init__(self, size):
        """Instantiation private var. size and
        using methods from the base class
        """
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method to find the area
        """
        return self.__size ** 2
