#!/usr/bin/python3
"""a function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class

    Args:
        obj: object
        a_class: instance of an object
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
