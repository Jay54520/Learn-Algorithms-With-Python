# -*- coding: utf-8 -*-
import unittest

from permutation import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        self.assertEqual([], s.Permutation(''))

    def test_not_empty(self):
        ss = 'abcc'
        want = ['abcc',
                'acbc',
                'accb',
                'bacc',
                'bcac',
                'bcca',
                'cabc',
                'cacb',
                'cbac',
                'cbca',
                'ccab',
                'ccba']
        got = s.Permutation(ss)
        self.assertEqual(want, got)
