#!/usr/bin/python3

class Square:
    """
    Square class represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position
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
        Prints the square using
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

