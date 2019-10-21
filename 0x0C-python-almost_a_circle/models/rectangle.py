#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            for z in range (self.__width):
                print('#', end='')
            print()


# here in __str__ you might need to find a way how to print name of the class
# Rectangle without hardcoding ot
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        lenght = len(args)

        if lenght == 1:
            for item in args:
                self.id = item
        if lenght == 2:
            for item in args:
                self.__width = item
        if lenght == 3:
            for item in args:
                self.__height = item
        if lenght == 4:
            for item in args:
                self.__x = item
        if lenght == 5:
            for item in args:
                self.__y = item
