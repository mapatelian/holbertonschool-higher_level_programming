#!/usr/bin/python3
for i in range(0, 9):
    for k in range(i + 1, 10):
        print("{:d}{:d}".format(i, k), end='')
        if i + k < 8 + 9:
            print(",", end=' ')
print()
