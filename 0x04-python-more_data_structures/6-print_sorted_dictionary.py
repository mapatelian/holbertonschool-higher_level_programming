#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints keys and values in a dictionary

        Args:
            a_dictionary (dict)
    """
    for key, val in sorted(a_dictionary.items()):
        print("{}: {}".format(key, val))
