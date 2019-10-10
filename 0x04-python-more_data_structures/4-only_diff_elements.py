#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function that looks for only unique elements in two sets

        Args:
            set_1 (set)
            set_2 (set)
        Return:
            newly created set
    """

    new1 = list(set_1) + list(set_2)
    new2 = []
    for i in set_1:
        for k in set_2:
            if i is k:
                new2.append(i)

    new3 = []
    for j in new1:
        for h in new2:
            if j is not h:
                new3.append(j)

    return new3
