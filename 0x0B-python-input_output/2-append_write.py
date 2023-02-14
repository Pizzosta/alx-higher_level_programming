#!/usr/bin/python3
"""Define a function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def append_file(filename="", text=""):
    """Function that appends to a text file

    Args:
        filename(str): name of file to write
        text(str): string chars to write to file

    Return:
        count of chars written
        function will create file if it doesn't exist

    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_text = f.write(text)
        return append_text
