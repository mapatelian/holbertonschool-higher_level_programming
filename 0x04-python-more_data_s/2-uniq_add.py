#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list
    result = 0
    set(new_list)
    for i in new_list:
        result = result + i
    return result
