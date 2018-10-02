# -*- coding: utf-8 -*-
import unittest
from .get_first_no_repeating_char import Solution, NOT_FOUND

s = Solution()


class Test(unittest.TestCase):

    def test_no_repeating_char(self):
        string = 'aa'
        got = s.FirstNotRepeatingChar(string)
        want = NOT_FOUND
        self.assertEqual(want, got)

    def test_repeating_char(self):
        string = 'ab'
        got = s.FirstNotRepeatingChar(string)
        want = 0
        self.assertEqual(want, got)

