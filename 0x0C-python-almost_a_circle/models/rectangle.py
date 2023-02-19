#!/usr/bin/python3
"""Module of a Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize child Class Rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): x coordinates
            y(int): y coordinates
            id(int): id of the rectangle
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """retrieves the width"""
            return self.__width

        @width.setter
        def width(self, value):
            """set the width"""
            self.__width = value

        @property
        def height(self):
            """retrieves the height"""
            return self.__height

        @height.setter
        def height(self, value):
            """set the height"""
            self.__height = value

        @property
        def x(self):
            """retrieves x coordinate"""
            return self.__x

        @x.setter
        def x(self, value):
            """set x coordinate"""
            self.__x = value

        @property
        def y(self):
            """retrieves y coordinate"""
            return self.__y

        @y.setter
        def y(self, value):
            """retrieves y coordinates"""
            self.__y = value
