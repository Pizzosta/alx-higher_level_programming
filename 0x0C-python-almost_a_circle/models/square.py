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
        """Updates and assigns new attributes to Square
        Args:
            *args (ints): new list of arguments (no-keyword-argument)
            1st arg (int): id attribute of Square
            2nd arg (int): size attribute of Square
            3rd arg (int): x attribute of Square
            4th arg (int): y attribute of Square
            **kwargs (dict): New key/value argument
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
