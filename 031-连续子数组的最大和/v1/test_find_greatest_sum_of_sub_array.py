# -*- coding: utf-8 -*-
import unittest
from .find_greatest_sum_of_sub_array import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            s.FindGreatestSumOfSubArray([])

    def test_all_negative(self):
        array = [-1, -2, -3]
        want = -1
        got = s.FindGreatestSumOfSubArray(array)
        self.assertEqual(want, got)

    def test_all_positive(self):
        array = [1, 2, 3]
        want = sum(array)
        got = s.FindGreatestSumOfSubArray(array)
        self.assertEqual(want, got)

    def test_positive_and_negative_with_current_sum_negative(self):
        array = [1, -2, 3]
        want = 3
        got = s.FindGreatestSumOfSubArray(array)
        self.assertEqual(want, got)

    def test_positive_and_negative_with_current_sum_positive(self):
        array = [3, -2, 3]
        want = 4
        got = s.FindGreatestSumOfSubArray(array)
        self.assertEqual(want, got)

    def test_starts_with_second_position(self):
        array = [-3, 2, 3]
        want = 5
        got = s.FindGreatestSumOfSubArray(array)
        self.assertEqual(want, got)
