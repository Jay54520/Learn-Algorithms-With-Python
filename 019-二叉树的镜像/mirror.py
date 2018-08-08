# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Mirror(self, root):
        """
        操作给定的二叉树，将其变换为源二叉树的镜像。

        输入描述:

        二叉树的镜像定义：

        源二叉树
                    8
                   /  \
                  6   10
                 / \  / \
                5  7 9 11

        镜像二叉树
                    8
                   /  \
                  10   6
                 / \  / \
                11 9 7  5

        算法：

        因为树的递归定义是 (L, S, R)，L、R 也是树，S 是一个节点。观察上方推导出算法为：

        循环条件：交换当前节点的左右子树，然后分别对左右子树调用当前方法。

        终止条件：当前节点为空，然后返回根节点。

        证明：

        二叉树的所有情况为：空、一个节点、多个节点。

        * 空节点：符合上述的终止条件，符合预期
        * 一个节点：交换了这个节点的左右子树，然后因为它的子树是空，所以触发了终止条件，然后返回，符合预期
        * 多个节点：我认为和镜像二叉树的定义一样，所以证明通过

        如果题目没有给出示例，那么我们要自己能画图出来。因为画图更直观，能跟容易帮助我们寻找规律。
        画图用电脑或文字也可以，上面的示例也算一种画图。

        :param root:
        :return:
        """
        if not root:
            return root

        # ---------- 交换根节点的左右子树 ------------
        left = root.left
        root.left = root.right
        root.right = left
        # ---------- 交换根节点的左右子树 ------------

        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
