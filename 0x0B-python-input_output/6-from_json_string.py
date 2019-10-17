#!/usr/bin/python3
import json
"""JSON module"""


def from_json_string(my_str):
    """Returns a Python data structure represented by a JSON string
        Args:
        my_str (str): Python data structure
    """
    return json.loads(my_str)
