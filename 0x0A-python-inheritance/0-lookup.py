#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """ Returns a List of an object's available attributes"""
    return (list(dir(obj)))
