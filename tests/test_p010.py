"""Unit tests for p10.py."""

import unittest

from src.p010 import sum_of_primes


class TestP10(unittest.TestCase):

    def test_exception(self):
        self.assertRaises(ValueError, sum_of_primes, 0)

    def test_expected(self):
        self.assertEqual(sum_of_primes(1), 0)
        self.assertEqual(sum_of_primes(2), 0)
        self.assertEqual(sum_of_primes(3), 2)
        self.assertEqual(sum_of_primes(4), 5)
        self.assertEqual(sum_of_primes(5), 5)
        self.assertEqual(sum_of_primes(6), 10)
        self.assertEqual(sum_of_primes(7), 10)
        self.assertEqual(sum_of_primes(8), 17)


if __name__ == '__main__':
    unittest.main()
