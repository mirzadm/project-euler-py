"""Unit tests for p11.py."""

import unittest

from src.p011 import grid_max_adjacent_elements_product as max_adj_prod


class TestP11(unittest.TestCase):
    
    def test_max_adj_prod_exception(self):
        grid = [[1, 2], [3, 4]]
        self.assertRaises(ValueError, max_adj_prod, grid, 3)
        self.assertRaises(ValueError, max_adj_prod, grid, 0)

    def test_max_adj_prod_1_by_1(self):
        grid = [[5]]
        self.assertEqual(max_adj_prod(grid, 1), 5)

    def test_max_adj_prod_2_by_2(self):
        grid = [[4, 0], [2, 3]]
        self.assertEqual(max_adj_prod(grid, 1), 4)
        self.assertEqual(max_adj_prod(grid, 2), 12)
        
        grid = [[0, 4], [3, 2]]
        self.assertEqual(max_adj_prod(grid, 1), 4)
        self.assertEqual(max_adj_prod(grid, 2), 12)


if __name__ == '__main__':
    unittest.main()
