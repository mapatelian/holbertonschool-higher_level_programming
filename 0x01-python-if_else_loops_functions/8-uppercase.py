#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            lower = ord(i)
            i = chr(lower - 32)
        print("{}".format(i), end='')
    print()
