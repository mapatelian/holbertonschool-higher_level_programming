#!/usr/bin/python3
"""Module that defines a new class
"""


class MyList(list):
    """New class MyList that inherits from list class
    """
    def print_sorted(self):
        """Method to print a sorted list
        """
        print(sorted(self))
