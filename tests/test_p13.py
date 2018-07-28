"""Unit tests for p13.py."""

import unittest

from src.p13 import add_num_str


class TestP13(unittest.TestCase):

    def test_exception(self):
        self.assertRaises(ValueError, add_num_str, '12', '34', 0)

    def test_expected(self):
        self.assertEqual(add_num_str('', '', 1), '')
        self.assertEqual(add_num_str('', '', 2), '')
        self.assertEqual(add_num_str('999', '', 1), '999')
        self.assertEqual(add_num_str('999', '', 2), '999')
        self.assertEqual(add_num_str('999', '', 3), '999')
        self.assertEqual(add_num_str('999', '', 4), '999')
        self.assertEqual(add_num_str('999', '0', 1), '999')
        self.assertEqual(add_num_str('999', '0', 2), '999')
        self.assertEqual(add_num_str('999', '0', 3), '999')
        self.assertEqual(add_num_str('999', '0', 4), '999')
        self.assertEqual(add_num_str('999', '1', 1), '1000')
        self.assertEqual(add_num_str('999', '1', 2), '1000')
        self.assertEqual(add_num_str('999', '1', 3), '1000')
        self.assertEqual(add_num_str('999', '1', 4), '1000')
        self.assertEqual(add_num_str('999', '999', 1), '1998')
        self.assertEqual(add_num_str('999', '999', 2), '1998')
        self.assertEqual(add_num_str('999', '999', 3), '1998')
        self.assertEqual(add_num_str('999', '999', 4), '1998')


if __name__ == '__main__':
    unittest.main()
