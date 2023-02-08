#!/usr/bin/python3
"""
Define function that checks inheritance of class object
"""



def inherits_from(obj, a_class):
    """Checks if the object is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
