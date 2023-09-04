#!/usr/bin/python3

""" Creating an empty Rectangle class"""


class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retreive width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Geter method to retreive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
