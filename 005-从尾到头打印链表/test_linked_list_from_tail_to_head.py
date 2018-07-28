# -*- coding: utf-8 -*-
import unittest

from linked_list_from_tail_to_head import Solution, ListNode

s = Solution()


class TestLinkedListFromTailToHead(unittest.TestCase):

    def test_success(self):
        third_node = ListNode(3, None)
        second_node = ListNode(2, third_node)
        head = ListNode(1, second_node)
        got = s.printListFromTailToHead(head)
        want = [3, 2, 1]
        self.assertEqual(got, want)

    def test_empty(self):
        self.assertEqual(s.printListFromTailToHead(None), [])