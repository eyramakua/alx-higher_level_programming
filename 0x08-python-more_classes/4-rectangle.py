#!/usr/bin/python3


"""creating an empty Rectangle class"""


class Rectangle:
    """class of a rectangle"""

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ("")

    rect = []
    for h in range(self.__height):
        [rect.append('#') for b in range(self.__width)]
        if h != self.__height - 1:
            rect.append("\n")
    return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " str(self.__height) + ")"
        return (rect)
