# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        """
        输入一个链表，输出该链表中倒数第k个结点。链表的尾节点是倒数第一个节点，比如
        [1, 2, 3, 4, 5, 6] 6 个节点，倒数第三个节点是值为 4 的节点。


        算法：

        题目没有对 k 的大小做出限制，那么这里定义，如果 k 大于链表的长度，那么返回 None。
        节点为 None，也返回 None。

        双指针，第二个指针比第一个指针后 k 个节点。这样当第二个指针到达 None 时，第一个指针就指向倒数
        第 k 个节点。如果第二个指针还没有比第一个后 k 就到了 None，那么说明 k 大于链表的长度，根据上方的定义返回 None。

        复杂度分析：

        时间复杂度：遍历一次 O(n)
        空间复杂度：O(1)
        """
        if not head:
            return None

        first_index = head
        second_index = head

        # 第二个指针移动 k 次
        for i in range(k):
            second_index = second_index.next
            # 第二个指针还没有比第一个后 k 就到了 None，那么说明 k 大于链表的长度，返回 None
            if second_index is None and i < k - 1:
                return None

        while second_index is not None:
            first_index = first_index.next
            second_index = second_index.next

        return first_index
