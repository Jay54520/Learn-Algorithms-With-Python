# -*- coding:utf-8 -*-
import unittest
from .left_rotate_string import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        got = s.LeftRotateString('', 1)
        want = ''
        self.assertEqual(want, got)

    def test(self):
        got = s.LeftRotateString('abcdefg', 9)
        want = 'cdefgab'
        self.assertEqual(want, got)
