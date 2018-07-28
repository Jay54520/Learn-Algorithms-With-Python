# -*- coding: utf-8 -*-
import unittest

from replace_space import Solution

s = Solution()


class TestReplaceSpace(unittest.TestCase):

    def test_1(self):
        string = "We Are Happy"
        got = s.replaceSpace(string)
        want = "We%20Are%20Happy"
        self.assertEqual(got, want)

    def test_empty(self):
        string = ""
        got = s.replaceSpace(string)
        want = ""
        self.assertEqual(got, want)
