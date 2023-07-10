#!/usr/bin/python3
"""Defines checking function"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of a given class

    Returns:
        if obj is exactly an instance of a_class then - True.
        else - False.
    """
    if type(obj) == a_class:
        return True
    return False
