#!/usr/bin/python3
def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a (int): first integer
        b (int): second integer

    Return:
        sum of the arguments

    """

    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, float) is False and isinstance(b, int) is False:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
