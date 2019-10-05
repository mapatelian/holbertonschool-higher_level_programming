#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            l = 0
            for k in i:
                print("{:d}".format(k), end='')
                if l != len(i) - 1:
                    print(" ", end='')
                    l += 1
            print()
