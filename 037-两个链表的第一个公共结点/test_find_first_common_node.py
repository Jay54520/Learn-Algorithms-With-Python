# -*- coding: utf-8 -*-
import unittest
from .find_first_common_node import Solution, ListNode


class Test(unittest.TestCase):

    def test_empty(self):
        got = Solution().FindFirstCommonNode(None, None)
        want = None
        self.assertEqual(want, got)

    def test(self):
        """
             1 -> 2 -> 3
                       \
             4 -> 5  -> 6 -> 7
        """
        one = ListNode(1)
        two = ListNode(2)
        three = ListNode(3)
        four = ListNode(4)
        five = ListNode(5)
        six = ListNode(6)
        seven = ListNode(7)
        one.next = two
        two.next = three
        three.next = six
        six.next = seven
        four.next = five
        five.next = six
        got = Solution().FindFirstCommonNode(one, four)
        want = six
        self.assertEqual(want, got)
