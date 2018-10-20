import unittest
from .str_to_int import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        want = 0
        got = s.StrToInt('')
        self.assertEqual(want, got)

    def test_positive(self):
        want = 123
        got = s.StrToInt('+123')
        self.assertEqual(want, got)

        got = s.StrToInt('123')
        self.assertEqual(want, got)

    def test_negative(self):
        want = -123
        got = s.StrToInt('-123')
        self.assertEqual(want, got)

    def test_invalid(self):
        want = 0
        got = s.StrToInt('-a123')
        self.assertEqual(want, got)
