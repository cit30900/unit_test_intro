import unittest
from shapes import Rectangle, Triangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(2, 2)
        self.r2 = Rectangle(3, 4)

    def test_area(self):

        self.assertEqual(self.r1.area, 4)
        self.assertEqual(self.r2.area, 12)
        self.assertGreater(self.r1.side1, 0)
        self.assertGreater(self.r1.side2, 0)
        self.assertGreater(self.r2.side1, 0)
        self.assertGreater(self.r2.side2, 0)

    def test_perimeter(self):

        self.assertEqual(self.r1.perimeter, 8)
        self.assertEqual(self.r2.perimeter, 14)

    def test_is_square(self):

        self.assertTrue(self.r1.is_square)
        self.assertFalse(self.r2.is_square)

if __name__ == '__main__':
    unittest.main()