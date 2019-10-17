#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Checkes whether an object is an instance of a specific class
    Args:
        obj: object to be checked
        a_class (class): a class
    Return:
        True or False
    """
    return isinstance(obj, a_class)
