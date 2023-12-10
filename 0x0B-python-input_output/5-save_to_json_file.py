#!/usr/bin/python3
"""
mosule that writes an object file using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """write an object file"""
    with open(filename, 'w') as open_file:
        open_fille.write(json.dumps(my_obj))
