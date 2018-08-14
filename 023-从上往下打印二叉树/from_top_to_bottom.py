# -*- coding:utf-8 -*-
import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    从上往下返回出二叉树的每个节点，同层节点从左至右返回。

    比如:
    1
    |\
    2 3
    | \
    4 5
    返回 [1, 2, 3, 4, 5]

    算法及证明：

    模拟：

    root, left, right, left_left, (left_right 为空，跳过), (right_left 为空，跳过),
    right_right, right_right 没有子节点，结束。

    发现这里需要保存先入先出的顺序，所以使用 queue。

    终止条件：

    当前的节点没有子节点。

    算法：

    空树，直接返回 []；

    非空树。将 root 加入队列
        循环：当队列不为空时：
            弹出队列中的第一个元素，将它的值加入结果中，将它的非空子节点按从左到右的顺序加入队列，
            然后进入下一个循环。
        终止条件：队列为空

    证明：

    1. 对于空树，符合要求；

    2.  根据队列的特性，先入先出：
    根节点是第一个进入的，所以第一个出来，符合要求；
    然后是根节点的非空子节点由左到右，也符合要求；
    然后是左节点的非空子节点由左到右，右节点的非空子节点由左到右，也符合要求；
    由于所有节点会依次加入队列，所以当队列为空时说明遍历完了，终止条件正确；

    证明通过。

    复杂度分析：
    时间复杂度：O(n)，遍历一次所有节点。
    空间复杂度：O(logn)，在队列中含有某一层的最多节点：2h - 1，由于 h = logn，所以复杂度为 O(logn)
    """

    def PrintFromTopToBottom(self, root):
        result = []
        if not root:
            return result

        queue = Queue.Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()  # type: TreeNode
            result.append(node.val)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        return result
