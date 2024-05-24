#!/usr/bin/python3
"""
Unittest for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_mixed_list(self):
        self.assertEqual(max_integer([1, 3, 7, 2, 5, 3]), 7)

    def test_all_same_elements(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_floats_and_integers(self):
        self.assertEqual(max_integer([1.1, 2, 3.3, 4]), 4)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 1000000]), 1000000)

if __name__ == '__main__':
    unittest.main()
