"""Unit tests for p016."""

import unittest

from src.p016 import calc_big_power_of_two


class TestP016(unittest.TestCase):

    def test_num_paths_in_grid(self):
        self.assertRaises(ValueError, calc_big_power_of_two, -1)
        self.assertEqual(calc_big_power_of_two(0), [1])
        self.assertEqual(calc_big_power_of_two(1), [2])
        self.assertEqual(calc_big_power_of_two(2), [4])
        self.assertEqual(calc_big_power_of_two(3), [8])
        self.assertEqual(calc_big_power_of_two(4), [6, 1])
        self.assertEqual(calc_big_power_of_two(5), [2, 3])
