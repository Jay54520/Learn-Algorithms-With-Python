import unittest
from .sum_solution import Solution

s = Solution()


class Test(unittest.TestCase):

    def test(self):
        got = s.Sum_Solution(4)
        want = 10
        self.assertEqual(want, got)
