# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, root1, root2):
        """
        root2 是否为 root1 的子树。空树不是任何树的子树。

        算法1：
        
        因为空树不是任何树的子树，所以只要存在一个空树，那么返回 False。
        
        证明：

        因为空树不是任何树的子树，所以只要存在一个空树，那么返回 False。
        证明如下：
        如果 root2 是空树，那么符合定义；
        如果 root1 是空树，root2 不是空树，也是 False。

        如果 root2 是 root1 的子树，由于子树的构造为 (左子树, 根节点, 右子树)，所以有以下三种情况：
        root2 是 root1 当前节点的子树；证明见 current_tree_has_subtree 的注释
        root2 是 root 左子树的子树；
        root2 是 root1 右子树的子树;

        复杂度分析：

        令 root1、root2 分别有 m、n 个节点，并且只有最后一个遍历的值不相同。

        时间复杂度：遍历 root1，对每个 root1 节点最多要比较 n 次，所以为 O(mn)
        空间复杂度：O(1)
        :param root1: TreeNode
        :param root2: TreeNode
        :return: bool
        """
        if not root1 or not root2:
            return False

        if self.current_tree_has_subtree(root1, root2):
            return True
        if self.HasSubtree(root1.left, root2):
            return True
        if self.HasSubtree(root1.right, root2):
            return True
        return False

    def current_tree_has_subtree(self, parent, sub):
        """
        sub 是否是当前 parent 的子树。

        两棵树所有对应位置都相等:
        * sub 不为空，parent 对应位置必须要不为空并且值相等
            * 两者对应子树也遵循这个关系
            * 如果都遵循，则返回 True
        * sub 为空，parent 可以为空或者不为空 -- 返回 True
        :param parent:
        :param sub:
        :return:
        """
        if sub:
            if parent and parent.val == sub.val:
                return self.current_tree_has_subtree(parent.left, sub.left) and self.current_tree_has_subtree(parent.right, sub.right)
            return False
        return True