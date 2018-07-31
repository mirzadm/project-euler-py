"""Unit tests for p14.py."""

import unittest

from src.p14 import calculate_sequence_length


class TestP14(unittest.TestCase):

    def test_calculate_sequence_length_exception(self):
        self.assertRaises(ValueError, calculate_sequence_length, 0, {})

    def test_calculate_sequence_length_expected(self):
        current_items = {}
        self.assertEqual(calculate_sequence_length(1, current_items), 1)

        current_items = {}
        self.assertEqual(calculate_sequence_length(2, current_items), 2)

        current_items = {}
        self.assertEqual(calculate_sequence_length(3, current_items), 8)

        current_items = {}
        self.assertEqual(calculate_sequence_length(4, current_items), 3)

        # 3 -> 10 -> 5
        current_items = {5: 500} 
        self.assertEqual(calculate_sequence_length(3, current_items), 502)


if __name__ == '__main__':
    unittest.main()
