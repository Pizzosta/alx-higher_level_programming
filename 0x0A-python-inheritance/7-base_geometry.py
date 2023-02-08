#!/usr/bin/python3
"""Define class BaseGeometry"""


class BaseGeometry:
    """define BaseGeometry"""

    def area(self):
        """define area of geometry - currently not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Instance validator

        Args:
            name(str): name of the object
            value(int): value of the object

        Exceptions:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
