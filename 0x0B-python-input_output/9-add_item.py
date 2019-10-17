#!/usr/bin/python3
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = 'add_item.json'
jslist = load_from_json_file(filename)

if len(sys.argv) > 1:
    for item in range(1, len(sys.argv)):
        jslist.append(sys.argv[item])
    save_to_json_file(jslist, filename)
