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
        
        如果 root2 是空树，那么符合定义；
        如果 root1 是空树，那么不可能存在 root2 是 root1 的空树，所以也是 False。

        因为树的递归定义是 (L, S, R)，L、R 也是树，S 是一个节点。前序遍历 root1，然后判断遍历时的树是否与
        root2 相等，如果相等，返回 True；如果遍历完也没有，那么返回 False。（这里令两棵树相同也算子树。）

        复杂度分析：

        令 root1、root2 分别有 m、n 个节点。

        时间复杂度：遍历 root1，对每个 root1 节点最多要比较 n 次（只有最后一个节点的值不一样），所以为 O(mn)
        空间复杂度：O(1)

        算法1是错误的。没有考虑到 {123} 可以是 {1234} 的子树。

        算法2：

        因为空树不是任何树的子树，所以只要存在一个空树，那么返回 False。这个在上面已经证明了。

        遍历 root1，判断 root2 是否为当前节点的子树，如果是，返回 True；遍历完成后还没有返回，说明没有找到，返回 False。

        复杂度分析：

        令 root1、root2 分别有 m、n 个节点。

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
        if root1:
            if self.HasSubtree(root1.left, root2):
                return True
        if root1:
            if self.HasSubtree(root1.right, root2):
                return True
        return False

    def current_tree_has_subtree(self, root1, root2):
        """
        root2 是否是当前 root1 的子树。

        循环条件：都不为空，两者根节点的值要相等，并且 root2 对应的子树也必须是 root1 对应子树的子树。

        终止条件： root1 或 root2 为空。
        如果都为空，返回 True；
        否则：
            如果只有 root2 为空，返回 True，说明在这里 root2 已经比完了；
            只有 root1 为空，返回 False，说明这里 root1 比 root2 少；

        :param root1:
        :param root2:
        :return:
        """
        if root1 and root2:
            if root1.val != root2.val:
                return False
            if not self.current_tree_has_subtree(root1.left, root2.left):
                return False
            if not self.current_tree_has_subtree(root1.right, root2.right):
                return False
        else:
            if not root1 and not root2:
                return True
            if root1 and not root2:
                return True
            if not root1 and root2:
                return False
        return True
