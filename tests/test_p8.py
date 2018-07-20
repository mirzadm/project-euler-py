"""Unit tests for p8.py."""

import unittest

from src.p8 import find_adj_digits_with_max_product as adj_digits


class TestP8(unittest.TestCase):

    def test_exception(self):
        self.assertRaises(ValueError, adj_digits, '', 1)

    def test_without_zeros(self):
        self.assertEqual(adj_digits('2', 1), (2, 0))
        self.assertEqual(adj_digits('12', 1), (2, 1))
        self.assertEqual(adj_digits('21', 1), (2, 0))
        self.assertEqual(adj_digits('23', 2), (6, 0))
        self.assertEqual(adj_digits('123', 2), (6, 1))

    def test_with_zeros(self):
        self.assertEqual(adj_digits('0', 1), (0, 0))
        self.assertEqual(adj_digits('00', 1), (0, 0))
        self.assertEqual(adj_digits('02', 1), (2, 1))
        self.assertEqual(adj_digits('20', 1), (2, 0))
        self.assertEqual(adj_digits('02', 2), (0, 0))
        self.assertEqual(adj_digits('20', 2), (0, 0))
        self.assertEqual(adj_digits('023', 2), (6, 1))


if __name__ == '__main__':
    unittest.main()