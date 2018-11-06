# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        输入两个（单向）链表，找出它们的第一个公共结点。
             1 -> 2 -> 3
                       \
             4 -> 5  -> 6 -> 7

        算法1：
        遍历第一个链表：
            在第二个链表中寻找第一个链表的节点
        复杂度分析：
        时间复杂度：假设两个链表分别由 m、n 个节点，那么为 O(mn)
        空间复杂度：O(1)

        算法2：
        公共节点是两个链表第一个相同的节点。
        将第一个链表的节点放到字典中。在 Python 中 set 和字典的效果一样，所以使用 set。
        遍历第二个链表，如果第二个链表的节点在字典中，那么这个节点就是公共节点。
        复杂度分析：
        时间复杂度：O(m + n)，遍历第一个链表 O(m)，遍历第二个链表 O(n)，所以为 O(m + n)
        空间复杂度：这里我们无法预先知道链表的长度，所以是 O(max(m, n))

        算法3：
        观察可以发现，公共节点是在链表的尾部。
        同时从后向前遍历两个链表，最后一个相同的节点就是第一个公共节点。
        由于是单向链表，所以为了从后向前遍历，就需要先将两个链表储存到栈中。
        复杂度分析：
        时间复杂度：O(max(m, n))
        空间复杂度：O(m + n)
        与算法2相比，时间、空间复杂度互换了。
        """
        if not pHead1 or not pHead2:
            return
        s = set()
        while pHead1:
            s.add(pHead1)
            pHead1 = pHead1.next

        while pHead2:
            if pHead2 in s:
                return pHead2
            pHead2 = pHead2.next
        return None