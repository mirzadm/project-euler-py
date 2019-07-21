"""Unit tests for p14.py."""

import unittest

from src.p014 import update_sequence_length_map


class TestP14(unittest.TestCase):

    def test_update_sequence_length_map_exception(self):
        self.assertRaises(ValueError, update_sequence_length_map, 0, {})

    def test_update_sequence_length_map_expected(self):
        sequence_map = {}
        self.assertEqual(update_sequence_length_map(1, sequence_map), {1: 1})

        sequence_map = {}
        self.assertEqual(
            update_sequence_length_map(2, sequence_map), {2: 2, 1: 1}
        )

        sequence_map = {}
        self.assertEqual(
            update_sequence_length_map(3, sequence_map),
            {3: 8, 10: 7, 5: 6, 16: 5, 8: 4, 4: 3, 2: 2, 1:1}
        )

        # 3 -> 10
        sequence_map = {10: 7}
        self.assertEqual(
            update_sequence_length_map(3, sequence_map),
            {3: 8, 10: 7}
        )
