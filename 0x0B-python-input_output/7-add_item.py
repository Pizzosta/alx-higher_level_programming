#!/usr/bin/python3
"""
Writes a script that adds all arguments from cmd line to a Python list
then saves to a JSON file.
"""
import sys

save_to_json_file = __import__('save_to_json_file').save_to_json_file
load_from_json_file = __import__('load_from_json_file').load_from_json_file
dd_item.py
try:
    py_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    py_list = []

py_list += sys.argv[1:]  # append items to list
save_to_json_file(py_list, add_item.json)  # save items to file
