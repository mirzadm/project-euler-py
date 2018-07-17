"""Unit tests for p6.py."""

import unittest

from src.p6 import square_of_sum_minus_sum_of_squares as square_sum_diff


class TestP6(unittest.TestCase):

    def test_square_sum_diff(self):
        self.assertRaises(ValueError, square_sum_diff, 0)
        self.assertEqual(square_sum_diff(1), 0)
        self.assertEqual(square_sum_diff(2), 4)
        self.assertEqual(square_sum_diff(3), 22)


if __name__ == '__main__':
    unittest.main()
