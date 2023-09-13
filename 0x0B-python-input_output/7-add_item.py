#!/usr/bin/python3
"""
Module that adds all argument to a python list
"""

import sys
import os

arg_list = sys.argv[1:]

save_JSON = __import__('5-save_to_json_file').save_to_json_file
load_JSON = __import__('6-load_from_json_file').load_from_json_file

listb = []
if os.path.exists('add_item.json'):
    listb = load_JSON('add_item.json')

save_JSON(listb + arg_list, "add_item.json")
