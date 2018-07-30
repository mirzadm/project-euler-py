"""Unit tests for p13.py."""

import unittest

from src.p13 import number_string_to_list, add_int_lists_with_carry


class TestP13(unittest.TestCase):

    def test_number_string_to_list_exception(self):
        self.assertRaises(ValueError, number_string_to_list, '123', 0)

    def test_number_string_to_list_expected(self):
        self.assertEqual(number_string_to_list('', 1), [])
        self.assertEqual(number_string_to_list('1', 1), [1])
        self.assertEqual(number_string_to_list('1', 2), [1])
        self.assertEqual(number_string_to_list('12', 1), [1, 2])
        self.assertEqual(number_string_to_list('12', 2), [12])
        self.assertEqual(number_string_to_list('12', 3), [12])
        self.assertEqual(number_string_to_list('1234567', 3), [1, 234, 567])
        self.assertEqual(number_string_to_list('100', 2), [1, 0])

    def test_add_int_lists_with_carry_exception(self):
        self.assertRaises(ValueError, add_int_lists_with_carry, [1], [2], 0)

    def test_add_int_lists_with_carry_expected(self):
        self.assertEqual(add_int_lists_with_carry([], [], 1), [])
        self.assertEqual(add_int_lists_with_carry([1], [], 1), [1])
        self.assertEqual(add_int_lists_with_carry([9], [1], 1), [1, 0])
        self.assertEqual(add_int_lists_with_carry([9], [1], 2), [10])
        self.assertEqual(add_int_lists_with_carry([9, 9], [1], 1), [1, 0, 0])
        self.assertEqual(add_int_lists_with_carry([9, 9], [1], 1), [1, 0, 0])




if __name__ == '__main__':
    unittest.main()
