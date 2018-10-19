import unittest
from .is_continous import Solution

s = Solution()


class Test(unittest.TestCase):

    def test_empty(self):
        got = s.IsContinuous([])
        want = False
        self.assertEqual(want, got)


    def test_true(self):
        got = s.IsContinuous([1, 3, 0, 0, 5])
        want = True
        self.assertEqual(want, got)

    def test_false(self):
        got = s.IsContinuous([1, 6, 0, 0, 5])
        want = False
        self.assertEqual(want, got)

    def test_pair(self):
        got = s.IsContinuous([1, 0, 0, 1, 0])
        want = False
        self.assertEqual(want, got)
