#!/usr/bin/python3
"""New module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """New class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding print
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieving size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setting width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating valies
        """
        mylist = ['id', 'size', 'x', 'y']
        if args:
            for i, item in enumerate(args):
                setattr(self, mylist[i], item)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of the class
        """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
