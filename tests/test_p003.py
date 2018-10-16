"""Unit tests for p3.py."""

import unittest

from src.p003 import largest_prime_factor


class TestP3(unittest.TestCase):

    def test_largest_prime_factor_exception(self):
        self.assertRaises(ValueError, largest_prime_factor, 1)

    def test_largest_prime_factor_expected(self):
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(3), 3)
        self.assertEqual(largest_prime_factor(4), 2)
        self.assertEqual(largest_prime_factor(5), 5)
        self.assertEqual(largest_prime_factor(22), 11)
        self.assertEqual(largest_prime_factor(100), 5)


if __name__ == '__main__':
    unittest.main()
