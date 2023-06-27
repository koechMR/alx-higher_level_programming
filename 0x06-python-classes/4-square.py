ass Square:
    """
    Square
    """

    def __init__(self, size=0):
        """
        Initializes a Square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size
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

    def area(self):
        """
        Calculates the area
        """
        return self.__size ** 2

