# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.traverse_results = []

    def Convert(self, pRootOfTree):
        """
        输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
        要求不能创建任何新的结点，只能调整树中结点指针的指向。

            10
            |   \
            6   14
            | \  |  \
            4 8  12 16

            4 <-> 6 <-> 8 <-> 10 <-> 12 <-> 14 <-> 16

            顺序就是二叉搜索树的中序遍历顺序，然后将它们串起来变成双向链表。

        算法：

        * 空，返回空
        * 非空，如上所述

        证明

        二叉搜索树的中序遍历结果就是从小到大。

        对于空树或者只有一个节点，显然符合；
        对于多个节点，根据树的结构，只需要证明

        1. 左子树的中序遍历是有序的、
        2. 右子树的中序遍历是有序的
        3. 根节点在它们之间

        根据二叉搜索树的定义，根节点大于左子树，小于右子树，所以 3 成立。

        由于左右子树也是二叉搜索树，所以 1、2 成立。

        复杂度分析

        时间复杂度：遍历 O(n)、生成链表 O(n)，所以为 O(n)
        空间复杂度：O(1)，遍历结果并没有创建新的对象，只是增加了引用计数，所以为 O(1)

        总结

        * 看到问题，觉得很复杂，束手无策。这意味着你没有想到合适的解法，因为算法题的思路
        都不会很复杂。
        * 看不懂“只能调整树中结点指针的指向”，以及对 Python 的变量传递机制不够清楚。
        一开始认为只能通过 left 或 right 操作，没有想到可以将 left = node.left
        也只是引用操作
        * 不知道二叉搜索树的中序遍历结果就是从小到大（维基百科上也没写）
        """
        if not pRootOfTree:
            return None

        self.middle_traverse(pRootOfTree)
        for index in range(len(self.traverse_results) - 1):
            cur_node = self.traverse_results[index]
            next_node = self.traverse_results[index + 1]
            cur_node.right = next_node
            next_node.left = cur_node
        return self.traverse_results[0]

    def middle_traverse(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.middle_traverse(pRootOfTree.left)
        self.traverse_results.append(pRootOfTree)
        self.middle_traverse(pRootOfTree.right)
