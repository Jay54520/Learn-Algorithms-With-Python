import unittest
from .add import Solution

s = Solution()


class Test(unittest.TestCase):

    def test(self):
        got = s.Add(1, 2)
        want = 3
        self.assertEqual(want, got)

    def test2(self):
        got = s.Add(111, 899)
        want = 1010
        self.assertEqual(want, got)
