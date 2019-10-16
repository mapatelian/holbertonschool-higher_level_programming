#!/usr/bin/python3
def lookup(obj):
    """
    Function to check all the available attributes and methods
    Args:
        obj: object to be checked
    Return:
        list of available attributes and methods of a given attribute
    """
    return dir(obj)
