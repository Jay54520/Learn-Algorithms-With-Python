# -*- coding:utf-8 -*-
class Solution:

    """
    定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数，并且使
    min、push 和 pop 操作的时间复杂度都为 O(1)。

    算法1：

    按正常的栈的算法实现，所以 push 和 pop 都为 O(1)；
    对于 min，每次在栈的所有元素中查找出最小值，时间复杂度为 O(n)，所以不符合要求。

    算法2：

    维持两个栈，一个正常栈，一个最小栈。最小栈的对应位置是正常栈那时候的最小值，最小栈和正常栈
    在 push 或 pop 时同时变化。

    push：
    如果栈为空，那么直接将元素放入两个栈中；
    否则，将新增值与目前的最小值比较，得出新增元素后的最小值，并将其加入最小栈。
    然后将新增元素放入普通栈。

    pop：同时从最小栈和正常栈中 pop
    min：最小栈的 top 元素

    由于要求了时间复杂度，而没有要求空间复杂度，所以可以通过增加空间复杂度来降低时间复杂度。
    对于这类方案，第一个想到的就是字典，但是没有想到合适的解法。由于想到的是储存栈的所有顺序状态，
    而没有优化为只储存栈的最小值的状态。而且储存方法是使用两个关联的 list 储存，而没有使用字典。

    复杂度：

    时间复杂度：O(1)，因为与上一个最小值比较是 1 次操作，append 是 O(1)。
    空间复杂度：O(n)，因为 min_stack 有 n 个元素。
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        if not self.stack:
            self.min_stack.append(node)
        else:
            min_value = self.min()
            if node < min_value:
                min_value = node
            self.min_stack.append(min_value)
        self.stack.append(node)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
