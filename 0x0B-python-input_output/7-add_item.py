#!/usr/bin/python3
"""
Writes a script that adds all arguments from cmd line to a Python list
then saves to a JSON file.
"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

py_list = []
if os.path.exists("add_item.json"):
    py_list[] = load_from_json_file("add_item.json")

for arg in sys.argv[1:]:  # append items to list
    py_list.append(arg)

save_to_json_file(py_list, "add_item.json")  # save items to file
