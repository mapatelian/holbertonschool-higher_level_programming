#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end='')
        except IndexError:
            leng = 0
            for k in my_list:
                leng += 1
            print()
            return leng
    print()
    return x
