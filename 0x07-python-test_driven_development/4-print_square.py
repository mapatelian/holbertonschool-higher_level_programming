#!/usr/bin/python3
def print_square(size):
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for k in range(size):
            print("#", end='')
        print()
