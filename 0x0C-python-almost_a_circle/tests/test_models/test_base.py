#!/usr/bin/python3
"""
Unittest for Base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit testing for Base Model"""

    def testing_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id)

    def testing_customid(self):
        base = Base(150)
        self.assertEqual(base.id, 150)

    if __name__ == '__main__':
        unittest.main()
