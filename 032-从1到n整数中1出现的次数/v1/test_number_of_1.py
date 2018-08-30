# -*- coding: utf-8 -*-
import unittest
from .number_of_1 import Solution

s = Solution()


class Test(unittest.TestCase):

    def tests(self):
        for n in [0, 13, 113, 3999, 27777]:
            want = self.loop_count(n)
            got = s.NumberOf1Between1AndN_Solution(n)
            self.assertEqual(want, got)

    def loop_count(self, n):
        """根据遍历计算，覆盖了所有情况，所以是正确的"""
        count = 0
        for num in range(n + 1):
            count += str(num).count('1')
        return count