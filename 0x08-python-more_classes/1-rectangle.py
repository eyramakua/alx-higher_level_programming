#!/usr/bin/python3

""" Creating an empty Rectangle class"""


class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """Getter method to retreive width"""
    def width(self):
        return.__width

    @width.setter
    """Property setter for width"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """Geter method to retreive height"""
    def height(self):
        return.__height

    @height.setter
    """Property setter for height"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
