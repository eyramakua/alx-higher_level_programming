#!/usr/bin/python3
"""
module for inherit
"""


def inherits_from(obj, a_class):
    """returns true if the object is an instance"""
    return isinstance(obj, a_class) and type(obj) != a_class
