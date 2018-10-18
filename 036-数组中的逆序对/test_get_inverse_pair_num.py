# -*- coding: utf-8 -*-
import unittest
from .get_inverse_pair_num import Solution


class Test(unittest.TestCase):

    def test(self):
        data = [7, 5, 6, 4]
        got = Solution().InversePairs(data)
        want = 5
        self.assertEqual(want, got)

    def test_empty(self):
        data = []
        got = Solution().InversePairs(data)
        want = 0
        self.assertEqual(want, got)