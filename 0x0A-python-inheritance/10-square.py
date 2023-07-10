#!/usr/bin/python3
"""Defines  Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rep a square"""

    def __init__(self, size):
        """Initializes a new square to be used

        Args:
            size (int): size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
