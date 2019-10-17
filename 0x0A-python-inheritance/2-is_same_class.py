#!/urs/bin/python3
def is_same_class(obj, a_class):
    """Checkes whether an object is an instance of a specific class
    Args:
        obj: object to be checked
        a_class (class): a class
    Return:
        True or False
    """
    if type(obj) == a_class:
        return True
    return False
