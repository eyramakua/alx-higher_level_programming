#!/usr/bin/python3
"""
module that creates an object file from JSON representation
"""


import json


def load_from_json_file(filename):
    """creating an object file"""
    with open(filename, 'r') as open_file:
        return json.load(open_file)
