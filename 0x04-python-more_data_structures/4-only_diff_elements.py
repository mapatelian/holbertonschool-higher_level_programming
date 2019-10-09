#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function that looks for only unique elements in two sets

        Args:
            set_1 (set)
            set_2 (set)
        Return:
            newly created set
    """
    new = []
    new = list(set_1) + list(set_2)
    return set(new)
