#!/usr/bin/python3
"""
Module that writes a class from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle defintion and working
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
 
    def type_value 

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def (self, value):
        return self.__height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def area(self):
        '''area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''print # to stdout'''
        print('\n' * self.y, end='')
        for h in range(self.height):
            print(' '* self.x + '#'*self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )

    def update(self, *args, **kwargs):
        expect = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                    args + expect[len(args):len(expect)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)
