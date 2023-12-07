#!/usr/bin/python3
"""
module forr BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Paises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(Self, name, value):
        """Validate"""
        if type(value) != int:
            raise TypeError(name + "must be an integer")
        if value <= 0:
            raise ValueError(name + "must be greater than 0")
