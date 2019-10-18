#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Multiplies all the dict values by 2
        Args:
            a_dictionary (dict): dictionary to be updated
    """
    return {key: value * 2 for (key, value) in a_dictionary.items()}
