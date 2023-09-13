#!/usr/bin/python3
"""
A JSON module representation
"""

import json


def from_json_string(my_str):
    """Return an object represented by JSON"""
    return json.loads(my_str)
