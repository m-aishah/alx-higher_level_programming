#!/usr/bin/python3
"""Unittest for Base class."""
import sys
sys.path.append('/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models')
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Unittests for Base class."""

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(None)
        self.b4 = Base(12)
        self.b5 = Base()

    def test_init(self):
        """Test the constructor."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)


if __name__ == '__main__':
    unittest.main()
