#!/usr/bin/python3
"""define class base"""


class Base:
    """Base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
