#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, 'w', encoding='utf-8') as filie:
        return json.load(filie)
