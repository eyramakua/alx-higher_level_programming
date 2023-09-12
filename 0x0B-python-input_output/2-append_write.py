#!/usr/bin/python3
"""
Module that appends a string and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a string and returns number of characters"""
    with open(filename, 'a', encoding='utf-8') as appender:
        number = appender.write(text)
    return number
