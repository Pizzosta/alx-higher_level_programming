#!/usr/bin/python3
"""a function that inserts a line of text to a file, 
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file

    Args:
        filename: filename
        search_string: search string to insert new line
        new_string: new string inserted
    """
    text = []
    with open(filename, 'r', encoding="utf-8") as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w', encoding="utf-8") as w:
        w.write(text)
