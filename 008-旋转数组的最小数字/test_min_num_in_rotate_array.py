# -*- coding: utf-8 -*-
import unittest

from min_num_in_rotate_array import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_rotate_array(self):
        rotate_array = [3, 4, 5, 1, 2]
        got = s.minNumberInRotateArray(rotate_array)
        want = 1
        self.assertEqual(got, want)

    def test_has_equal_elements(self):
        rotate_array = [5, 5, 1, 2, 3, 4]
        got = s.minNumberInRotateArray(rotate_array)
        want = 1
        self.assertEqual(got, want)

    def test_rotate_zero(self):
        rotate_array = list(range(5))
        got = s.minNumberInRotateArray(rotate_array)
        want = 0
        self.assertEqual(got, want)

    def test_one_element(self):
        rotate_array = [1]
        got = s.minNumberInRotateArray(rotate_array)
        want = 1
        self.assertEqual(got, want)
