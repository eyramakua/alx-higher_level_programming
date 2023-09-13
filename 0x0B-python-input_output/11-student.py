#!/usr/bin/python3
"""
Module that writes a class
"""


class Student:
    '''Student class'''

    def __init__(self, first_name, last_name, age):
        '''Initialize a class'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves dictonary to JSON'''
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            ret = {}
            for h, j in self.__dict__.items():
                if h in attrs:
                    ret[h] = j
            return ret
        else:
            return self.__dict__

    def reload_from_json(self, json):
        '''Change attributes'''
        for h, j in json.items():
            self.__dict__[h] = j
