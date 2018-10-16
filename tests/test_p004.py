"""Unit tests for p4.py."""

import unittest

from src.p004 import is_palindrome, convert_num_to_digits_list


class TestLargestPalindrome(unittest.TestCase):

    def test_convert_num_to_digits_list(self):
        self.assertRaises(ValueError, convert_num_to_digits_list, -1)
        self.assertEqual(convert_num_to_digits_list(0), [0])
        self.assertEqual(convert_num_to_digits_list(1), [1])
        self.assertEqual(convert_num_to_digits_list(12), [2, 1])
        self.assertEqual(convert_num_to_digits_list(123), [3, 2, 1])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(-1))
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(123))


if __name__ == '__main__':
    unittest.main()
