"""Unit tests for p019."""

import unittest

from src.p019 import is_leap_year, days_in_year, days_in_month


class TestCase(unittest.TestCase):

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(0))
        self.assertTrue(is_leap_year(4))
        self.assertTrue(is_leap_year(8))
        self.assertTrue(is_leap_year(400))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1))
        self.assertFalse(is_leap_year(2))
        self.assertFalse(is_leap_year(3))
        self.assertFalse(is_leap_year(5))
        self.assertFalse(is_leap_year(10))
        self.assertFalse(is_leap_year(100))
        self.assertFalse(is_leap_year(1900))
