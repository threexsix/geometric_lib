import unittest
from math import pi
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_positive_value(self):
        result = area(1)
        self.assertAlmostEqual(result, 1 * 1 * pi, 5)

    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            area(-123)

    def test_area_zero_value(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_perimeter_positive_value(self):
        result = perimeter(1)
        self.assertAlmostEqual(result, 2 * 1 * pi, 5)

    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            perimeter(-123)

    def test_perimeter_zero_value(self):
        result = perimeter(0)
        self.assertEqual(result, 0)