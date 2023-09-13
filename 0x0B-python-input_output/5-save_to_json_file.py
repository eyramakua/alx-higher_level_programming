#!/usr/bin/python3
"""
Module that writes an object file using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object file"""
    with open(filename, 'w') as open_file:
        open_file.write(json.dumps(my_obj))
