#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Updating a dictionary.

        Args:
            a_dictionary (dict): dictionary to be updated
            key (str): new key
            value (str): new value
        Return: updated dictionary
    """
    a_dictionary.update({key: value})
    return a_dictionary
