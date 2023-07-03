#!/usr/bin/python3

class Square:
    """
<<<<<<< HEAD
    Square class represents a square
=======
    Square class

    Attributes:
        __size (int):
        __position (tuple):
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square
<<<<<<< HEAD
=======

        Args:
            size (int):
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
<<<<<<< HEAD
        Getter method
=======
        Getter method.

        Returns:
            int: The size
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
<<<<<<< HEAD
        Setter method to set the size
=======
        Setter method

        Args:
            value (int):
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
<<<<<<< HEAD
        Getter method to retrieve the position
=======
        Getter method
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
<<<<<<< HEAD
        Setter method to set the position
=======
        Setter method to set

        Args:
            value (tuple):
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value) or any(num < 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area
        """
        return self.__size ** 2

    def my_print(self):
        """
<<<<<<< HEAD
        Prints the square using
=======
        Prints the square
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

