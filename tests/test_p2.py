"""Unit tests for p2.py."""

import unittest

from src.p2 import sum_of_even_fibo_nums


class TestSumOfFibo(unittest.TestCase):

    def test_sum_of_even_fibo_nums(self):
        self.assertEqual(sum_of_even_fibo_nums(1), 1)
        self.assertEqual(sum_of_even_fibo_nums(2), 2)
        self.assertEqual(sum_of_even_fibo_nums(3), 2)
        self.assertEqual(sum_of_even_fibo_nums(4), 2)
        self.assertEqual(sum_of_even_fibo_nums(5), 2)
        self.assertEqual(sum_of_even_fibo_nums(6), 2)
        self.assertEqual(sum_of_even_fibo_nums(7), 2)
        self.assertEqual(sum_of_even_fibo_nums(8), 10)


if __name__ == '__main__':
    unittest.main()
