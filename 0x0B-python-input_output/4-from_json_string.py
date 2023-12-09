#!/usr/bin/python3
"""
A JSON module reprsentation
"""


import json


def from_json_string(my_str):
    """return an object reprsented by JSON"""
    return json.loads(my_str)
