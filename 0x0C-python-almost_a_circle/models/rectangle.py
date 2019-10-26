#!/usr/bin/python3
"""Module that initializes a new class
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retriveing width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width validator and setter
        """
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieving height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height validator and setter
        """
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieving x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """X validator and setter
        """
        if isinstance(value, int) is not True:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieving y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Y validator and setter
        """
        if isinstance(value, int) is not True:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Computing area
        """
        return self.__width * self.__height

    def display(self):
        """Displays area with the '#' key,
            according to the x- and y-axis
        """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            for z in range(self.__width):
                print('#', end='')
            print()


# here in __str__ you might need to find a way how to print name of the class
# Rectangle without hardcoding ot
    def __str__(self):
        """Overriding __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updating class Rectangle: assignment an argument to each attribute
            with the non-keyworded arguments
        """

        mylist = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, item in enumerate(args):
                setattr(self, mylist[i], item)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of the class
        """
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}
