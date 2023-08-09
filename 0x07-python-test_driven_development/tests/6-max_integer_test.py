#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([..])."""

    def test_empty_list(self):
        """Test an empty list."""
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        test_list = [10]
        self.assertEqual(max_integer(test_list), 10)

    def test_max_at_beginning(self):
        """Test a list with maximum value at the beginning."""
        test_list = [30, 20, 10, 5, 0]
        self.assertEqual(max_integer(test_list), 30)

    def test_max_at_middle(self):
        """Test a list with max value in between."""
        test_list = [2, 3, 10, 5, 6]
        self.assertEqual(max_integer(test_list), 10)

    def test_max_at_end(self):
        """Test a list with max value at the end."""
        test_list = [2, 3, 10, 5, 6, 100]
        self.assertEqual(max_integer(test_list), 100)

    def test_negative_list(self):
        """Test lists with negative numbers."""
        test_list = [-10, -9, -8, -7, -6]
        self.assertEqual(max_integer(test_list), -6)

    def test_ordered_list(self):
        """Test ordered lists."""
        test_list = [60, 61, 72, 73]
        self.assertEqual(max_integer(test_list), 73)

    def test_unordered_list(self):
        """Test unordered list."""
        test_list = [2, -1, 0, 89, 3]
        self.assertEqual(max_integer(test_list), 89)


if __name__ == '__main__':
    unittest.main()
