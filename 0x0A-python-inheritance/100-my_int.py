#!/usr/bin/python3
"""Define MyInt that inherits from int"""


class MyInt(int):
    """inverts operators == and !="""
    def __eq__(self, value):
        """invert == operator with != operator

        Args:
            value(int): object value to invert
        """
        return int.__ne__(self, value)

    def __ne__(self, value):
        """invert != operator with == operator

        Args:
            value(int): abject value to be invert
        """
        return int.__eq__(self, value)
