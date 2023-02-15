#!/usr/bin/python3
"""Module of class Student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Iniatializes a student class

        Args:
            first_name: first name of std
            last_name: last name of std
            age: age of std
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
