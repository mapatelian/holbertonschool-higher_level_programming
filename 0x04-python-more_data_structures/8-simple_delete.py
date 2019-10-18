#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes keys in dictionary
        Args:
            a_dictionary (dict): a dictionary to be edited
    """
    a_dictionary.pop(key, None)
    return a_dictionary
