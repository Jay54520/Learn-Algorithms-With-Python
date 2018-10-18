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
        将第一个链表的节点放到字典中。在 Python 中 set 和字典的效果一样，所以使用 set。
        遍历第二个链表，如果第二个链表的节点在字典中，那么这个节点就是公共节点。
        复杂度分析：
        时间复杂度：O(max(m, n))
        空间复杂度：O(min(m, n))，这里我们无法预先知道链表的长度，所以还是 O(max(m, n))

        算法3：
        观察可以发现，公共节点是在链表的尾部。
        同时从后向前遍历两个链表，最后一个相同的节点就是第一个公共节点。
        由于是单向链表，所以为了从后向前遍历，就需要先将两个链表储存到栈中。
        复杂度分析：
        时间复杂度：O(max(m, n))
        空间复杂度：O(m + n)
        所以不如算法2。所以最优算法是算法2。
        """
        if not pHead1 or not pHead2:
            return
        set1 = set()
        current1 = pHead1
        while current1:
            set1.add(current1)
            current1 = current1.next
        current2 = pHead2
        while current2:
            if current2 in set1:
                return current2
            current2 = current2.next
        return