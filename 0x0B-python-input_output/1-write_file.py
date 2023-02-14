#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of characters """
    with open(filename, 'w', encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
