#!/usr/bin/python3
import json
"""JSON module"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file (JSON repr.)
        Args:
            my_obj: Pythion data struct
            filename (str): name of the file
    """
    with open(filename, 'w') as filie:
        json.dump(my_obj, filie)
