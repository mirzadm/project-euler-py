"""Unit tests for p9.py."""

import unittest

from src.p9 import special_pythagorean_triple as pyth_triple


class TestP9(unittest.TestCase):

    def test_pyth_triple(self):
        self.assertIsNone(pyth_triple(10))
        self.assertEqual(pyth_triple(12), (3, 4, 5))
        self.assertEqual(pyth_triple(30), (5, 12, 13))


if __name__ == '__main__':
    unittest.main()
