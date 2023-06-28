#!/usr/bin/python3

"""Define a class"""


class Square:
    """Rep a square"""

    def __init__(self, size):
        """Init new square.

        Args:
            size (int): size of new square
        """
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
        """Return current area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with # character."""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
