#!/usr/bin/python3
"""Define rectangle that inherits from BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square from a Rectangle"""

    def __init__(self, size):
        """Initializes a square

        Args:
            size: size of the square
        """
        self.__size = size

        self.integer_validator("size", size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
