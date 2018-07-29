# -*- coding:utf-8 -*-

class Stack:

    def __init__(self):
        self._list = []

    def push(self, node):
        self._list.append(node)

    def pop(self):
        if self.is_empty():
            raise ValueError("Can't pop from empty stack")
        element = self._list[-1]
        self._list = self._list[:-1]
        return element

    def is_empty(self):
        if self._list:
            return False
        else:
            return True


class Solution:
    """
    用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

    算法分析及证明

    栈是后进先出，队列是先进先出。设有两个栈 stack_a、stack_b。

    假设数据都放入 stack_a 中，那么队列要取出的数据就是 stack_a 最下面的元素。如果取出一个
    元素后，栈为空，那么这个元素就是最下面的元素。由于只能使用栈来实现，所以 stack_a 弹出的数据
    要储存到 stack_b 中。这时 stack_a 为空，stack_b 中的元素顺序与它们加入时的顺序相反，
    也就是队列要求的顺序。所以可以优化为：如果 stack_b 中有数据，直接从 stack_b pop，否则，才像上面
    那样做。虽然这样做不能优化时间复杂度。

    复杂度

    时间复杂度

    push() 只要将新元素放入 stack_a 中，为 O(1)。
    pop() 要将 n - 1 个元素从 stack_a 转移到 stack_b，所以为 O(n)

    空间复杂度：没有额外消耗，所以为 O(1)。
    """

    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def push(self, node):
        self.stack_a.push(node)
        return

    def pop(self):
        if not self.stack_b.is_empty():
            return self.stack_b.pop()

        while not self.stack_a.is_empty():
            self.stack_b.push(self.stack_a.pop())
        result = self.stack_b.pop()
        return result
