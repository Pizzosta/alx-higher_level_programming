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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0c')
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """retrieves x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x coordinate"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """retrieves y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """retrieves y coordinates"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        """String & print representation of the rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))

    def update(self, *args):
        """Update the class Rectangle

        Arg:
            *args - new attributes:
                1st argument is id attribute
                2nd argument is width attribute
                3rd argument is height attribute
                4th argument is x attribute
                5th argument is y attribute
        """
        if args and len(args) != 0:
            a = 0

            for arg in args:
                if a == 0:
                    if id is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg

                a += 1
