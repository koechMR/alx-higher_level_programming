#!/usr/bin/python3
"""Defines class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent  rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Init a new Rectangle

        Args:
            width (int): The width of new Rectangle.
            height (int): The height of new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return then print() and str() that represents Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
