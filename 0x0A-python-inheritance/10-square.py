#!/usr/bin/python3
"""Module that initializes a new class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New class Square that inherits from class Rectangle
    """
    def __init__(self, size):
        """Instantiation private var. size,
        using methods from the base class
        """
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method to find the area
        """
        return self.__size ** 2
