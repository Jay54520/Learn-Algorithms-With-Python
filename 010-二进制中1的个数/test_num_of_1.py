# -*- coding: utf-8 -*-
import unittest

from number_of_1 import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(s.NumberOf1(3), 2)

    def test_zero(self):
        self.assertEqual(s.NumberOf1(0), 0)

    def test_negative(self):
        self.assertEqual(s.NumberOf1(-3), 63)
