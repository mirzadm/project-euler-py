"""Unit tests for p015."""

import unittest

from src.p015 import num_paths_in_grid


class TestP015(unittest.TestCase):

    def test_num_paths_in_grid(self):
        self.assertEqual(num_paths_in_grid(0, 0), 1)
        self.assertEqual(num_paths_in_grid(0, 1), 1)
        self.assertEqual(num_paths_in_grid(0, 2), 1)
        self.assertEqual(num_paths_in_grid(0, 100), 1)
        self.assertEqual(num_paths_in_grid(1, 0), 1)
        self.assertEqual(num_paths_in_grid(2, 0), 1)
        self.assertEqual(num_paths_in_grid(100, 0), 1)
        self.assertEqual(num_paths_in_grid(1, 1), 2)
        self.assertEqual(num_paths_in_grid(1, 2), 3)
        self.assertEqual(num_paths_in_grid(2, 1), 3)
        self.assertEqual(num_paths_in_grid(2, 2), 6)
