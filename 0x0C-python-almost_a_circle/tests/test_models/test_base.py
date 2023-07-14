#!/usr/bin/python3
"""define unittes for base.py"""

import os
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id_with_argument(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_id_increment(self):
        b5 = Base()
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()
