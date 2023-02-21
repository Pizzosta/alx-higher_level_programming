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
