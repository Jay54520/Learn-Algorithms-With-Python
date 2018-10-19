# -*- coding:utf-8 -*-
import unittest
from .reverse_sentence import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        got = s.ReverseSentence('')
        want = ''
        self.assertEqual(want, got)

    def test(self):
        got = s.ReverseSentence('I am a student.')
        want = 'student. a am I'
        self.assertEqual(want, got)