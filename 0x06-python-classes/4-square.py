<<<<<<< HEAD
ass Square:
    """
    Square
    """

    def __init__(self, size=0):
        """
        Initializes a Square
        """
=======
#!/usr/bin/python3

"""Define  class"""


class Square:
    """Rep class of  a square."""

    def __init__(self, size=0):
        """Init a new square.

        Args:
            size (int): size """
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        self.size = size

    @property
    def size(self):
<<<<<<< HEAD
        """
        Getter method to retrieve the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size
        """
=======
        return (self.__size)

    @size.setter
    def size(self, value):
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
<<<<<<< HEAD
        """
        Calculates the area
        """
        return self.__size ** 2

=======
        """return area of square"""
        return (self.__size * self.__size)
>>>>>>> 372900be2ac24fe63bf060dd11ba60dec6853653
