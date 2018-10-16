"""Unit tests for p7.py."""

import unittest

from src.p007 import nth_prime_number


class TestP7(unittest.TestCase):

    def test_nth_prime_number_exception(self):
        self.assertRaises(IndexError, nth_prime_number, 0)

    def test_nth_prime_number_expected(self):
        self.assertEqual(nth_prime_number(1), 2)
        self.assertEqual(nth_prime_number(2), 3)
        self.assertEqual(nth_prime_number(3), 5)
        self.assertEqual(nth_prime_number(4), 7)
        self.assertEqual(nth_prime_number(5), 11)
        self.assertEqual(nth_prime_number(6), 13)


if __name__ == '__main__':
    unittest.main()
