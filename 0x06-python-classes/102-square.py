#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Represents a class square"""
    def __eq__(self, other):
        return self.__size == other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __init__(self, size=0):
        """Initializes new square.

        Args:
            size(int): Size of the new square

        """
        self.__size = size

    @property
    def size(self):
        """Retrieve size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method returns the current square area"""
        return (self.__size * self.__size)
