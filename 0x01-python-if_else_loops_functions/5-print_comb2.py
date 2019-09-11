#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, 10):
        if i + k != 18:
            print("{:d}{:d}, ".format(i, k), end='')
print("{:d}".format(99))
