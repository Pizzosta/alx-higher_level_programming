#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """appends a string to a text file and returns the number of characters """
    with open(filename, 'a', encoding="utf-8") as f:
        append_text = f.append(text)
        return append_text
