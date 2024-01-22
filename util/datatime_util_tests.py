import unittest
import numpy as np
from datetime_utils import *

class TestTimeFunctions(unittest.TestCase):

    def test_fractional_hour(self):
        self.assertEqual(fractional_hour(1, 30, 0), 1.5)
        self.assertEqual(fractional_hour(0, 45, 30), 0.7583333333333333)
        self.assertEqual(fractional_hour(23, 0, 0), 23)

    def test_calculate_hour_sin_cos(self):
        hour_sin, hour_cos = calculate_hour_sin_cos(6)
        self.assertAlmostEqual(hour_sin, np.sin(np.pi / 2))
        self.assertAlmostEqual(hour_cos, np.cos(np.pi / 2))

    def test_get_actual_hour(self):
        hour_sin, hour_cos = calculate_hour_sin_cos(15)
        self.assertEqual(get_actual_hour(hour_sin, hour_cos), 15)

    def test_get_fractional_hour(self):
        hour_sin, hour_cos = calculate_hour_sin_cos(15.5)
        self.assertAlmostEqual(get_fractional_hour(hour_sin, hour_cos), 15.5, places=2)

    def test_fractional_hour_to_hms(self):
        hours, minutes, seconds = fractional_hour_to_hms(15.75)
        self.assertEqual(hours, 15)
        self.assertEqual(minutes, 45)
        self.assertEqual(seconds, 0)

if __name__ == '__main__':
    unittest.main()