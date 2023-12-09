#!/usr/bin/python3
"""
Module that reads text files
"""


def read_file(filename=""):
    """Reads content of file and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as reader:
        print(reader.read(), end="")
