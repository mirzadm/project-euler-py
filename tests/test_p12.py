"""Unit tests for p12.py."""

import unittest

from src.p12 import triangular_number_generator, find_special_triangular_num


class TestP12(unittest.TestCase):
    
    def test_triangular_number_generator(self):
        triangular_nums = []
        for i in triangular_number_generator():
            triangular_nums.append(i)
            if len(triangular_nums) == 5:
                break
        self.assertEqual(triangular_nums, [1, 3, 6, 10, 15])

    def test_find_special_triangular_num(self):
        self.assertEqual(find_special_triangular_num(5), 28)


if __name__ == '__main__':
    unittest.main()
