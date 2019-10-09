#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Function that looks for common elements in two sets

        Args:
            set_1 (set)
            set_2 (set)
        Return:
            New list with common elements
    """
    new = []

    for i in set_1:
        for k in set_2:
            if i is k:
                new.append(i)
    return new
