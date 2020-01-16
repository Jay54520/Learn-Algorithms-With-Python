# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    def Clone(self, pHead):
        """
        输入一个复杂链表（每个节点中有节点值，以及两个指针，
        一个指向下一个节点，另一个特殊指针指向任意一个节点），
        返回结果为复制后复杂链表的head。
        （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

        node1 -> node2 -> node3

        node1.random = node3
        node2.random = node1
        node3.random = node2

        算法：

        v1 中的空间复杂度是 O(n)，由于空间复杂度是最差情况下除了结果外占用的复杂度，
        所以如果采用相同的数据结构——链表储存旧节点 random 到新节点 random 的关系，
        就可以减少空间复杂度。

        按照上面的思路，将新节点插入到旧节点后面，比如：

        old_n1 -> new_n1 -> old_n2 -> new_n2 -> old_n3 -> new_n3

        则新旧节点的关系为：

        1. new_n = old_n.next
        2. 根据上面可以推断出：
            如果 new_n.random 不为 None: new_n.random = old_n.random.next。假设
            old_n.random = old_random，则 old_random.next = new_random。
            否则，当 new_n.random 为 None 时，old_n.random 也为 None

        根据第 2 点设置好新链表的 random：

        设置 random：

            * 新链表的头是第二个节点
            * new_n.next 是当前链表的 next.next
            * 终止条件是 old_cur 为 None

        拆分：
            拆分出新、旧链表。拆分出旧链表的原因是尽量不要改变函数的输入，并且
            牛客网的测试用例会根据输入来判断新链表是否引用了原链表。

            代码就是解释。
            终止条件是 old_index is None

        复杂度分析：
        时间复杂度：O(n)
        空间复杂度：O(1)

        总结

        * 通过与结果相同的数据结构来储存关系从而避免了空间的占用
        * 牛客网的判例有问题，返回的结果正确的情况下，因为输入被改变了，就判定错误，
        而我认为改变输入只是算编码规范问题而不算正确性问题。
        """
        if not pHead:
            return None

        # insert new next to old
        old_index = pHead
        while old_index:
            new = RandomListNode(old_index.label)
            old_index.next, new.next = new, old_index.next
            old_index = new.next

        # insert random
        old_index = pHead
        while old_index:
            if old_index.random:
                new = old_index.next
                new.random = old_index.random.next
            old_index = old_index.next.next

        # split new and restore old
        new_head = pHead.next
        old_index = pHead
        while old_index:
            new_index = old_index.next
            next_old_index = new_index.next
            next_new_index = next_old_index.next if next_old_index else None
            old_index.next, new_index.next = new_index.next, next_new_index
            old_index = next_old_index
        return new_head