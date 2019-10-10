#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function that looks for only unique elements in two sets

        Args:
            set_1 (set)
            set_2 (set)
        Return:
            newly created set
    """

    list_1 = list(set_1)
    list_2 = list(set_2)

    return [i for i in list_1 + list_2 if i not in list_1 or i not in list_2]
