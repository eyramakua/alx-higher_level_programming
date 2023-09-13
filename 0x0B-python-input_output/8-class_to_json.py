#!/usr/bin/python3
"""
Module that return dictionary description
"""


def class_to_json(obj):
    """Returns dictionary description"""
    return obj.__dict__
