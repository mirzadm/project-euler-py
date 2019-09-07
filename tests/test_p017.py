"""Unit tests for p017."""

import unittest

from src.p017 import num_to_words


class TestP017(unittest.TestCase):

    def test_num_to_words(self):
        self.assertRaises(ValueError, num_to_words, -1)
        self.assertRaises(ValueError, num_to_words, 1001)
        self.assertEqual(num_to_words(0), "zero")
        self.assertEqual(num_to_words(10), "ten")
        self.assertEqual(num_to_words(11), "eleven")
        self.assertEqual(num_to_words(20), "twenty")
        self.assertEqual(num_to_words(29), "twenty nine")
        self.assertEqual(num_to_words(99), "ninety nine")
        self.assertEqual(num_to_words(100), "one hundred")
        self.assertEqual(num_to_words(101), "one hundred and one")
        self.assertEqual(num_to_words(110), "one hundred and ten")
        self.assertEqual(num_to_words(111), "one hundred and eleven")
        self.assertEqual(num_to_words(199), "one hundred and ninety nine")
        self.assertEqual(num_to_words(999), "nine hundred and ninety nine")
        self.assertEqual(num_to_words(1000), "one thousand")
