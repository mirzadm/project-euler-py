"""Unit tests for p013."""

import unittest

from src.p013 import sum_str_nums


class TestP013(unittest.TestCase):
    def test_sum_str_nums(self):
        step = 0
        self.assertRaises(ValueError, sum_str_nums, "12", "34", step)
        step = 1
        self.assertEqual(sum_str_nums("0", "0", step), "0")
        self.assertEqual(sum_str_nums("1", "1", step), "2")
        self.assertEqual(sum_str_nums("9", "1", step), "10")
        self.assertEqual(sum_str_nums("10", "0", step), "10")
        self.assertEqual(sum_str_nums("10", "1", step), "11")
        self.assertEqual(sum_str_nums("99", "1", step), "100")
        self.assertEqual(sum_str_nums("99", "99", step), "198")
        self.assertEqual(sum_str_nums("100", "99", step), "199")
        self.assertEqual(sum_str_nums("100", "99", step), "199")
        self.assertEqual(sum_str_nums("100", "99", step), "199")
        self.assertEqual(sum_str_nums("101", "99", step), "200")
        step = 10
        self.assertEqual(sum_str_nums("0", "0", step), "0")
        self.assertEqual(sum_str_nums("1", "1", step), "2")
        self.assertEqual(sum_str_nums("9", "1", step), "10")
        self.assertEqual(sum_str_nums("10", "0", step), "10")
        self.assertEqual(sum_str_nums("10", "1", step), "11")
        self.assertEqual(sum_str_nums("99", "1", step), "100")
        self.assertEqual(sum_str_nums("99", "99", step), "198")
        self.assertEqual(sum_str_nums("100", "99", step), "199")
        self.assertEqual(sum_str_nums("100", "99", step), "199")
        self.assertEqual(sum_str_nums("100", "99", step), "199")
        self.assertEqual(sum_str_nums("101", "99", step), "200")
