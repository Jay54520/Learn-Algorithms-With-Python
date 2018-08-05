# -*- coding: utf-8 -*-
import unittest

from merge import Solution, ListNode

s = Solution()


class Test(unittest.TestCase):

    """
    所有类型的情况有：
    * 两个链表都为空
    * 一个为空，另一个不为空
    * 两个都不为空
    """

    def test_two_empty(self):
        got = s.Merge(None, None)
        want = None
        self.assertEqual(got, want)

    def test_half_empty(self):
        first_node = ListNode(1)
        second_node = ListNode(2)
        third_node = ListNode(3)
        first_node.next = second_node
        second_node.next = third_node

        got = s.Merge(first_node, None)
        want = [1, 2, 3]
        self.assertEqual(self.traverse_list_node(got), want)
        
    def test_not_empty(self):
        list1_first_node = ListNode(1)
        list1_second_node = ListNode(3)
        list1_third_node = ListNode(5)
        list1_first_node.next = list1_second_node
        list1_second_node.next = list1_third_node

        list2_first_node = ListNode(2)
        list2_second_node = ListNode(4)
        list2_third_node = ListNode(6)
        list2_first_node.next = list2_second_node
        list2_second_node.next = list2_third_node

        got = s.Merge(list1_first_node, list2_first_node)
        want = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.traverse_list_node(got), want)

    def traverse_list_node(self, list_node):
        result = []
        while list_node:
            result.append(list_node.val)
            list_node = list_node.next
        return result

