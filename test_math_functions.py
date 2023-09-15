import unittest
import math_functions


class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_functions.add(10, 5), 15)
        self.assertEqual(math_functions.add(-1, 1), 0)
        self.assertEqual(math_functions.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(math_functions.subtract(10, 5), 5)
        self.assertEqual(math_functions.subtract(-1, 1), -2)
        self.assertEqual(math_functions.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(math_functions.multiply(10, 5), 50)
        self.assertEqual(math_functions.multiply(-1, 1), -1)
        self.assertEqual(math_functions.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(math_functions.divide(10, 5), 2)
        self.assertEqual(math_functions.divide(-1, 1), -1)
        self.assertEqual(math_functions.divide(-1, -1), 1)
        self.assertEqual(math_functions.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            math_functions.divide(10, 0)

if __name__ == '__main__':
    unittest.main()