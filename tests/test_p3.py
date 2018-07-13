"""Unit tests for p3.py."""

import unittest

from src.p3 import is_prime, prime_numbers_up_to, largest_prime_factor


class TestLagrestPrimeFactor(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(10, [2, 3]))
        self.assertTrue(is_prime(11, [2, 3]))
        self.assertFalse(is_prime(100, [2, 3, 5, 7]))

    def test_prime_numbers_up_to(self):
        self.assertEqual(prime_numbers_up_to(2), [2])
        self.assertEqual(prime_numbers_up_to(3), [2, 3])
        self.assertEqual(prime_numbers_up_to(10), [2, 3, 5, 7])
        self.assertEqual(prime_numbers_up_to(19), [2, 3, 5, 7, 11, 13, 17, 19])


    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(3), 3)
        self.assertEqual(largest_prime_factor(4), 2)
        self.assertEqual(largest_prime_factor(5), 5)
        self.assertEqual(largest_prime_factor(6), 3)
        self.assertEqual(largest_prime_factor(7), 7)
        self.assertEqual(largest_prime_factor(8), 2)
        self.assertEqual(largest_prime_factor(9), 3)
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(66), 11)
        self.assertEqual(largest_prime_factor(67), 67)


if __name__ == '__main__':
    unittest.main()
