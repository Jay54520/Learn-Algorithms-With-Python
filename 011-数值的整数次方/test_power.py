# -*- coding: utf-8 -*-
import unittest

from power import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_positive(self):
        got = s.Power(2, 3)
        want = 8
        self.assertEqual(got, want)

    def test_zero(self):
        got = s.Power(2, 0)
        want = 1
        self.assertEqual(got, want)

    def test_negative(self):
        got = s.Power(2, -3)
        want = 1 / 8
        self.assertEqual(got, want)
