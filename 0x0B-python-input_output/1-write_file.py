#!/usr/bin/python3
"""
Module that writes a string to text
file and returns number of character written
"""


def write_file(filename="", text=""):
    """writes a string to a text and returns the number of character"""
    with open(filename, 'w' encoding='utf-8') as writer:
        number = writer.write(text)
    return number
