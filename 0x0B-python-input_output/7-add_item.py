#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
and then save them to a file
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def my_list():
    """
    reads existing json file and loads list,
    adds arguments to python list and saves to file
    """
    obj_list = load_from_json_file(filename)
    filename = "add_item.json"

    for i in range(1, len(sys.argv)):
        obj_list.append(str(sys.argv[i]))

    save_to_json_file(obj_list, filename)


filename = "add_item.json"
if len(sys.argv) < 2:
    try:
        f = open(filename)
        filename.close()
    except IOError:
        save_to_json_file([], filename)
else:
    try:
        f = open(filename)
        filename.close()
        my_list()
    except IOError:
        save_to_json_file([], filename)
        my_list()
