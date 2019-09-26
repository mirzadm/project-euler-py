"""Unit tests for p018."""

import unittest

from src.p018 import max_length_to_every_bottom_element as max_length


class TestCase(unittest.TestCase):

    def test_max_length(self):
        self.assertEqual(max_length([]), [])
        self.assertEqual(max_length([1]), [1])
        self.assertEqual(max_length([1, 2, 3]), [3, 4])
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6]), [7, 9, 10])
        self.assertEqual(max_length(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [14, 17, 19, 20]
        )
        self.assertEqual(max_length(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [4, 4, 4, 4]
        )
