# -*- coding: utf-8 -*-
import unittest

from reverse_list import Solution, ListNode

s = Solution()


class Test(unittest.TestCase):

    def test_three_nodes(self):
        first_node = ListNode(1)
        second_node = ListNode(2)
        third_node = ListNode(3)
        first_node.next = second_node
        second_node.next = third_node

        got = s.ReverseList(first_node)

        self.assertEqual(got.val, 3)
        self.assertEqual(got.next.val, 2)
        self.assertEqual(got.next.next.val, 1)
        self.assertEqual(got.next.next.next, None)

    def test_empty(self):
        self.assertEqual(s.ReverseList(None), None)

    def test_one_node(self):
        head = ListNode(1)
        got = s.ReverseList(head)
        want = head
        self.assertEqual(got, want)