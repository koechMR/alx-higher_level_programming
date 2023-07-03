#!/usr/bin/python3

<<<<<<< HEAD
class Square:
    """
<<<<<<< HEAD
    Square class represents
=======
    Square class represents a square.

    Attributes:
        __size (int):
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
    """

    def __init__(self, size=0):
        """
<<<<<<< HEAD
        Init
=======
        Initializes a Square instance.

        Args:
            size (int):
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
=======
"""Define Square"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Init new square

        Args:
            size (int): size of the new square
>>>>>>> origin/master
        """
        self.size = size

    @property
    def size(self):
<<<<<<< HEAD
        """
<<<<<<< HEAD
        Getter method
=======
        Getter method to retrieve
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        return self.__size
=======
        return (self.__size)
>>>>>>> origin/master

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
<<<<<<< HEAD
        """
<<<<<<< HEAD
        Calculates the area
=======
        Calculates the area of the square.
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        return self.__size ** 2
=======
        """Return current area of square"""
        return (self.__size * self.__size)
>>>>>>> origin/master

    def my_print(self):
        """Print square with the # character"""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
