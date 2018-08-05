# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def ReverseList(self, pHead):
        """
        输入一个链表，反转链表后，输出新链表的表头。
        如果输入是 [1, 2, 3, 4, 5, 6]，那么输出是 [6, 5, 4, 3, 2, 1]

        算法与证明：

        1. 如果链表为 None，那么返回 None
        2. 双指针（previous、current）遍历链表，将当前节点的下一个指向前一个节点。定义头节点的前一个节点为 None。由于这里是遍历，
        所以可以处理到节点数目大于 0 的所有情况。终止条件为当前节点为 None，这时的 previous 就是要返回的节点

        复杂度分析：

        时间复杂度：O(n) 遍历一次链表
        空间复杂度：O(1)

        :param pHead: ListNode
        :return: ListNode
        """
        if pHead is None:
            return None

        previous = None
        current = pHead
        while current is not None:
            # 这里叫 next_node 而不是 next 是因为 next 与自带的变量名冲突了
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous