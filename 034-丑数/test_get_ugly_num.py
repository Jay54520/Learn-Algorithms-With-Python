# -*- coding: utf-8 -*-
import unittest
from .get_ugly_num import Solution

s = Solution()


class Test(unittest.TestCase):

    def test(self):
        index_want = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
        }
        for index, want in index_want.items():
            got = s.GetUglyNumber_Solution(index)
            self.assertEqual(want, got)