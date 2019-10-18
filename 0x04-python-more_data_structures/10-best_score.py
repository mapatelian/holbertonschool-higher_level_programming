#!/usr/bin/python3
def best_score(a_dictionary):
    """Looks for the key in dictionary with the biggest int value
        Args:
            a_dictionary (dict)
        Return:
            key corresponding to the biggest value
    """
    my_list = []
    best = 0
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        my_list.append(key)
        my_list.append(value)

    for item in range(len(my_list)):
        if isinstance(my_list[item], int) is True and my_list[item] > best:
            best = my_list[item]
            name = my_list[item - 1]
    return name
