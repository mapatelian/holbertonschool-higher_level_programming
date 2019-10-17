#!/usr/bin/python3
import json
"""JSON module"""


def to_json_string(my_obj):
    """JSON representation of an object
        Args:
            my_obj: object to be encoded
        Return: JSON string
    """
    return json.dumps(my_obj)
