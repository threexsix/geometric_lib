import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_positive_value(self):
        result = area(2)
        self.assertAlmostEqual(result, 4, 5)

    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            area(-123)

    def test_area_zero_value(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_perimeter_positive_value(self):
        result = perimeter(2)
        self.assertAlmostEqual(result, 8, 5)

    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            perimeter(-123)

    def test_perimeter_zero_value(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_perimeter_string_value(self):
        with self.assertRaises(TypeError):
            area("hahahaha")
