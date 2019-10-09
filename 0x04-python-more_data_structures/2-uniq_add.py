#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Function that add up all the unique items in a list

    Args:
        my_list (list)
    Return:
        sum of the unique elements
    """
    result = 0
    new = set(my_list)
    for i in new:
        result = result + i
    return result
