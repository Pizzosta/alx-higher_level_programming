#!/usr/bin/python3
"""Define rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define child class of BaseGeometry"""

    def __init__(self, width, height):
        """Initializes Rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
