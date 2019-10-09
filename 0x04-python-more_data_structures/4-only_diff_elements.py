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
    for i in set_1:
        for k in set_2:
            if i is k:
                new.append(i)

    new1 = list(set_1) + list(set_2)

    new2 = []

    for j in new1:
        for u in new:
            if j is not u:
                new2.append(j)

    return new2
