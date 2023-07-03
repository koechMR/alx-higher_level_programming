#!/usr/bin/python3

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
        """
        self.size = size

    @property
    def size(self):
        """
<<<<<<< HEAD
        Getter method
=======
        Getter method to retrieve
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set

        Args:
            value (int):
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
<<<<<<< HEAD
        Calculates the area
=======
        Calculates the area of the square.
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

