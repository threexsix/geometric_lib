import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_positive_value(self):
        result = area(1, 2)
        self.assertAlmostEqual(result, 2, 5)

    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            area(-123, 24)

    def test_area_zero_value(self):
        result = area(0, 1)
        self.assertEqual(result, 0)

    def test_perimeter_positive_value(self):
        result = perimeter(1, 2)
        self.assertAlmostEqual(result, 2 * (1 + 2), 5)

    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            perimeter(-123, 124)

    def test_perimeter_zero_value(self):
        result = perimeter(0, 0)
        self.assertEqual(result, 0)
