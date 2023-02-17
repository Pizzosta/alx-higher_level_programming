#!/usr/bin/python3
"""Module of a Base Class"""


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base Class

        Args:
            id: value of the attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
