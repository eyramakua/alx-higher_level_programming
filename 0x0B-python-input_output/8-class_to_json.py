#!/usr/bin/python3
"""
module that reutrns dictionary description
"""


def class_to_json(obj):
    """returns dictionary description"""
    return obj.__dict__
