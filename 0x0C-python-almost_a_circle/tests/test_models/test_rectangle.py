#!/usr/bin/python3
"""Module documentation"""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Test class for the Rectangle class"""

    def setUp(self):
        """resets the __nb_objects back to zero
        before starting any test case"""

        self.__nb_objects = 0

    def test_rectangle(self):
        """tests the Rectangle class"""

        r1 = Rectangle(10, 3)

        self.assertEqual(r1.id, 1)

        r1 = Rectangle(2, 10)

        self.assertEqual(r1.id, 2)

        r1 = Rectangle(10, 2, 0, 0, 15)

        self.assertEqual(r1.id, 12)

        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 3)

        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 3, -1)

        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 3, 1, -1)

        with self.assertRaises(TypeError):
            r1 = Rectangle("Hello", 2)

        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "Hello")

    def test_area(self):
        """tests the area method in the Rectangle class"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_str(self):
        """test the __str__() method"""

        r4 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r4.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """updates the Rectangle attributes"""

        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89)
        self.assertEqual(r5.id, 89)

        r5.update(89, 2)
        self.assertEqual(r5.width, 2)

        r5.update(89, 2, 3, 4, 5)
        self.assertEqual(r5.x, 4)

    if __name__ == "__main__":
        unittest.main()
