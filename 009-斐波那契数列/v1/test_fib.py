# -*- coding: utf-8 -*-
import unittest

from fib import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_init(self):
        self.assertEqual(s.Fibonacci(0), 0)
        self.assertEqual(s.Fibonacci(1), 1)

    def test_fib(self):
        got = s.Fibonacci(4)
        want = 3
        self.assertEqual(got, want)
