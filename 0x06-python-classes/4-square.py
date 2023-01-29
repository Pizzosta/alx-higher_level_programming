#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Represents a class square"""

    def __init__(self, size=0):
        """Initializes new square.

        Args:
            size(int): Size of the new square

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Method returns the current square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Retrieve size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
