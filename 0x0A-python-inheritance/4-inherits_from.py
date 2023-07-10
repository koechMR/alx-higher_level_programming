#!/usr/bin/python3
"""Defines inherit from"""


def inherits_from(obj, a_class):
    """checks if an object has inherit

return:
if obj inherit instance of a class - true
else - false
"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
