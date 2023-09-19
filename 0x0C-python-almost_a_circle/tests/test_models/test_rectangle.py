#!/usr/bin/python3
"""
Unittest for base
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Defining unit testing for Rectangle model"""

    def testing_rectangle(self):
        r1 = Rectangle(2, 5)
        self.assertEqual(r1.id, Rectangle.__Base__nb_objects)
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.id, Rectangle.__Base__nb_objects)

if __name__ == '__main__':
    unittest.main()
