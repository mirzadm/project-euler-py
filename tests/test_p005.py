"""Unit tests for p5.py."""

import unittest

from src.p005 import prime_factorization, smallest_divisible_number


class TestP5(unittest.TestCase):

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(1), {})
        self.assertEqual(prime_factorization(2), {2: 1})
        self.assertEqual(prime_factorization(3), {3: 1})
        self.assertEqual(prime_factorization(4), {2: 2})
        self.assertEqual(prime_factorization(5), {5: 1})
        self.assertEqual(prime_factorization(6), {2: 1, 3: 1})

    def test_smallest_divisible_number(self):
        self.assertEqual(smallest_divisible_number(1), 1)
        self.assertEqual(smallest_divisible_number(2), 2)
        self.assertEqual(smallest_divisible_number(3), 6)
        self.assertEqual(smallest_divisible_number(4), 12)
        self.assertEqual(smallest_divisible_number(5), 60)


if __name__ == '__main__':
    unittest.main()
