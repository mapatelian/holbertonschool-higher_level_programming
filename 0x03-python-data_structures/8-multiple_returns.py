#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = tuple()
    if sentence:
        my_tuple = (len(sentence), sentence[0])
        return my_tuple
    else:
        my_tuple = (0, None)
        return my_tuple
