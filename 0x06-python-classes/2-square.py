#!/usr/bin/python3
"""Defines a square class."""


def __init__(self, size=0):
    """Initializes new square.

    Args:
        size(int): Size of the new square

    """
    self.__size = size

    if not isinstance(size, int):
        raise  TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        return (int(size))
