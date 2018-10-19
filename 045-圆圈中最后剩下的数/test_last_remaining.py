import unittest
from .last_remaining import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_zero(self):
        got = s.LastRemaining_Solution(0, 0)
        want = -1
        self.assertEqual(want, got)


    def test(self):
        got = s.LastRemaining_Solution(5, 3)
        want = 3
        self.assertEqual(want, got)

