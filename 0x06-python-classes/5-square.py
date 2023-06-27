#!/usr/bin/python3

class Square:
    """
    Square class represents a square.

    Attributes:
        __size (int):
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int):
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve
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
        Calculates the area of the square.
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

