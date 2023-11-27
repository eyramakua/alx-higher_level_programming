#!/usr/bin/python3


class Rectangle:
    """class of a Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
