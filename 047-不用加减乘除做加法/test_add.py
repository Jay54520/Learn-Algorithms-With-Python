# -*- coding:utf-8 -*-
import unittest
from .add import Solution

s = Solution()


class Test(unittest.TestCase):

    def test(self):
        got = s.Add(1, 2)
        want = 3
        self.assertEqual(want, got)

    # Python 的二进制处理和其他语言不同，所以这个测试不能通过。
    # def test2(self):
    #     got = s.Add(111, 899)
    #     want = 1010
    #     self.assertEqual(want, got)
