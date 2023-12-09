#!/usr/bin/python3
"""
Module that appends a string and returns no of character
"""


def append_write(filename="", text=""):
    """appends a string and returns no of character"""
    with open(filename, 'a', encoding='utf-8') as appender:
        number = appender.write(text)
    return number
