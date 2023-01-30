#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Represents a class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes new square.

        Args:
            size(int): Size of the new square
            position(int): position of the square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set position of the square"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end="")
                print()
