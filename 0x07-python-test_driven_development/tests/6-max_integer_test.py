#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test class for max_integer function"""

    def test_empty_list(self):
        """Checks for an empty list"""

        self.assertEqual(max_integer([]), None)

    def test_max_value(self):
        """Checks if the correct value is returned"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)


if __name__ == "__main__":
    unittest.main()
