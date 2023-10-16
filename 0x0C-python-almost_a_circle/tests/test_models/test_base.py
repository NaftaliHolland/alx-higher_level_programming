#!/usr/bin/python3
"""This is a test"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test class for the Base class"""

    def setUp(self):
        """runs before each test case
        creates and instance of Base"""
        self.base = Base()
        self.base2 = Base(12)

    def tearDown(self):
        """deletes the object created after a test is finished"""
        del self.base
        del self.base2

    def test_base(self):
        my_id = self.base.id
        self.assertEqual(my_id, 1)
        
        my_id = self.base2.id
        self.assertEqual(my_id, 12)

        with self.assertRaises(TypeError):
            base3 = Base(23, 53)


    if __name__ == "__main__":
        unittest.main()
