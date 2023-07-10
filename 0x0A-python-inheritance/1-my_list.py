#!/usr/bin/python3
"""define the MyList class"""


class MyList(list):
    """a sub-class of list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
