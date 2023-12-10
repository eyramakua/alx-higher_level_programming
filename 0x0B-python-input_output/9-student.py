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

    def to_json(self):
        '''Retrieves dictonary representation'''
        return self.__dict__
