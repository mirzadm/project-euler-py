"""Unit tests for p1.py."""

import unittest

from src.p1 import sum_of_multiples_3_or_5


class TestSumOfMultiples(unittest.TestCase):

    def test_sum_of_multiples(self):
        self.assertEqual(sum_of_multiples_3_or_5(0), 0)
        self.assertEqual(sum_of_multiples_3_or_5(4), 3)
        self.assertEqual(sum_of_multiples_3_or_5(6), 8)
        self.assertEqual(sum_of_multiples_3_or_5(10), 23)
        self.assertEqual(sum_of_multiples_3_or_5(11), 33)
        self.assertEqual(sum_of_multiples_3_or_5(12), 33)
        self.assertEqual(sum_of_multiples_3_or_5(13), 45)


if __name__ == '__main__':
    unittest.main()
