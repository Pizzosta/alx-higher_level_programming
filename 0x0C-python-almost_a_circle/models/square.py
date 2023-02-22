#!/usr/bin/python3
"""Module of a Square that inherits from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square

        Args:
            size(int): size of the square
            x(int): x coordinates
            y(int): y coordinates
            id(int): id

        Return:
            raise TypeError if attribute is not an integer
            raise ValueError if attribute is less than or equal to zero
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """String & Print representation"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    def update(self, *args, **kwargs):
        """Update the class Square
        Arg:
            *args - new attributes:
                1st argument is id attribute
                2nd argument is width attribute
                3rd argument is height attribute
                4th argument is x attribute
                5th argument is y attribute
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
