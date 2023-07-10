#!/usr/bin/python3
"""defines class square"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Compute and return the area of the rectangle.

        Returns:
            int: The computed area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: The formatted string describing the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
