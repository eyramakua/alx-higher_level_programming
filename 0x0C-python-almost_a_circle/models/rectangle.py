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
