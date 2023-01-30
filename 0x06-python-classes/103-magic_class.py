#!/usr/bin/python3
import math


class MagicClass:
    """ Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    """ Method that calculates the area of the circumference """
    def area(self):
        return (self.__radius ** 2 * math.pi)

    """ Method that calculates the perimeter of a circumference """
    def circumference(self):
        return (2 * math.pi * self.__radius)
