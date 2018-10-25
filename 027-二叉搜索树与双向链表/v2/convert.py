# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

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

        算法及证明

        将左子树转换为链表、左子树最大节点与根节点连接
        将右子树转换为链表，根节点与右子树最小节点连接

        左子树的最大节点是最右的那个节点，如果它没有右子树，那么就是它本身，
        因为右子树的节点比根节点大，所以最右就是最大；；

        右子树的最小节点是最左的那个节点，如果它没有左子树，那么就是它本身，
        因为左子树的节点比根节点小，所以最左就是最小；

        转换完成后，调整 pRootOfTree 到链表头部，因为如果有左子树，
        那么 pRootOfTree 就不是在头部。

        终止条件：

        * 为空，返回空
        * 叶子节点，返回该节点

        复杂度分析

        时间复杂度：O(n)
        空间复杂度：O(1)，相比 V1 少了中序遍历
        """
        if not pRootOfTree:
            return None

        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        if pRootOfTree.left:
            converted_left = self.Convert(pRootOfTree.left)
            max_left = self.get_max_left(converted_left)
            max_left.right = pRootOfTree
            pRootOfTree.left = max_left

        if pRootOfTree.right:
            converted_right = self.Convert(pRootOfTree.right)
            min_right = self.get_min_right(converted_right)
            pRootOfTree.right = min_right
            min_right.left = pRootOfTree

        # 移动 pRootOfTree 到链表的头部
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

    def get_max_left(self, converted_left):
        while converted_left.right:
            converted_left = converted_left.right
        return converted_left

    def get_min_right(self, converted_right):
        while converted_right.left:
            converted_right = converted_right.left
        return converted_right
