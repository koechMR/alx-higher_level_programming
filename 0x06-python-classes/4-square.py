#!/usr/bin/python3

"""Define  class"""


class Square:
    """Rep class of  a square."""

    def __init__(self, size=0):
        """Init a new square.

        Args:
            size (int): size """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of square"""
        return (self.__size * self.__size)
