#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """Returns list sorted in ascending order

    Args:
        list(int) - elements of the list
    """
    def __init__(self):
        """ Initialize MyList Object"""
        super().__init__()

    def print_sorted(self):
        """Returns sorted list"""
        print(sorted(self))
