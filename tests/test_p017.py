"""Unit tests for p017."""

import unittest

from src.p017 import (
    two_digit_num_to_words as two_digit,
    three_digit_num_to_words as three_digit,
)


class TestP017(unittest.TestCase):

    def test_two_digit(self):
        self.assertRaises(ValueError, two_digit, -1)
        self.assertRaises(ValueError, two_digit, 100)
        self.assertEqual(two_digit(0), "zero")
        self.assertEqual(two_digit(10), "ten")
        self.assertEqual(two_digit(11), "eleven")
        self.assertEqual(two_digit(20), "twenty")
        self.assertEqual(two_digit(29), "twenty nine")
        self.assertEqual(two_digit(99), "ninety nine")

    def test_three_digit(self):
        self.assertRaises(ValueError, three_digit, -1)
        self.assertRaises(ValueError, three_digit, 1000)
        self.assertEqual(three_digit(0), "zero")
        self.assertEqual(three_digit(10), "ten")
        self.assertEqual(three_digit(11), "eleven")
        self.assertEqual(three_digit(20), "twenty")
        self.assertEqual(three_digit(29), "twenty nine")
        self.assertEqual(three_digit(99), "ninety nine")
        self.assertEqual(three_digit(100), "one hundred")
        self.assertEqual(three_digit(101), "one hundred and one")
        self.assertEqual(three_digit(111), "one hundred and eleven")
        self.assertEqual(three_digit(999), "nine hundred and ninety nine")
