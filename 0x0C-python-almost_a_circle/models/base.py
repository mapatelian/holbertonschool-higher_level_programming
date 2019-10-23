#!/usr/bin/python3
"""Module that initializes a new class
"""


import json


class Base:
    """New class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts doct to a string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    # work on this one
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string to a file
        """
        if list_objs is None:
            mylist = []
        else:
            filename = "{}.json".format(cls.__name__)
            with open(filename, 'w', encoding='utf-8') as filie:
                json.dump(list_objs, filie)

    @staticmethod
    def from_json_string(json_string):
        """List of JSON representation
        """
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)
