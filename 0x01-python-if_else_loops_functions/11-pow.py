#!/usr/bin/python3
def pow(a, b):
    result = 1

    if b == 0:
        result = 1
    elif b == 1:
        result = a
    elif b >= 2:
        for i in range(b):
            result = result * a
    elif b < 0:
        b = b * -1
        for i in range(b):
            result = result * a
        result = 1 / result

    return result
