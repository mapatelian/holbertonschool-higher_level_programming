#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Checkes if an object is a subclass instance
    Args:
        obj: object to be checked
        a_class (class): a class
    Return:
        True or False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
