# -*- coding:utf-8 -*-
class Solution:
    """
    输入两个整数序列，判断能否通过对第一个序列执行 push 或 pop 操作（push 的元素必须按照序列的顺序，
    可以随时执行 pop）获取第二个序列（pop 结果的顺序应该与第二个序列相同）。假设压入栈的所有数字均不相等，两个序列的长度是相等的。

    比如 [1, 2, 3, 4, 5] => [4, 3, 5, 2, 1]：

    操作    第一个栈 结果
    push(1) [1]    []
    push(2) [1, 2] []
    push(3) [1, 2, 3] []
    push(4) [1, 2, 3, 4] []
    pop() [1, 2, 3] [4] []
    pop() [1, 2] [4, 3] []
    push(5) [1, 2, 5] [4, 3]
    pop() [1, 2] [4, 3, 5]
    pop()
    pop() [] [4, 3, 5, 2, 1]

    如果是 [4, 3, 5, 1, 2] 的话，那么不可能。因为对于状态 [1, 2] [4, 3, 5]，
    所有数字已经入栈了，而下一个要弹出的数字是 1，所以不可能。

    算法及证明：

    1. 根据题意，只有当 pop() 的结果与目标数字相等时，才可以 pop()
    2. 根据题意，只有当 pushV 还有未 push 的元素时，才可以 push()
    3. 当所有 pop() 的结果满足 popV 时，返回 True

    如果在还没有满足所有 popV 之前，既不能 push() 也不能 pop()，那么说明不可能。因为
    栈只可以执行 push() 或 pop() 操作。

    当可以 pop() 时，只能执行 pop()，因为由题意可知所有数字均不相同，所以目标数字不会在之后的入栈数字中了。

    初始情况，栈是空的，由于栈是空的，所以不能执行 pop()，只能执行 push()；
    push() 后，栈里有一个数，这时有两种选择：继续 push() 或 pop()：
        * 如果栈顶数字等于目标数字。根据上方的推论，只能执行 pop()，
        所以这里只能执行 pop() ，这时候栈为空，目标数字右移指向 popV 的第二个数字；
        * 否则，栈顶数字不等于目标数字，所以不能执行 pop()
            * 如果 pushV 里没有剩余数字了，那么不能执行 push() ，又因为不能执行 pop()，
            所以无法执行任何操作，所以不可能；
            * 如果 pushV 里还有剩余数字，那么只能 push()。这时候栈里共有两个元素。
                * 然后重复上面“如果栈顶数字等于目标数字。”的判断。

    终止条件：

    stack.pop 的结果符合所有 popV，返回 True；
    否则，栈顶数字不等于目标数字，并且没有剩余数字了，返回 False。

    当为空时，初始索引和长度相同，不会发生判断，直接返回 True，满足条件。

    复杂度：

    时间复杂度：O(n)。假设只有最后一个数字不符合，那么要 push n 次，pop (n - 1) 次，所以为 O(n)
    空间复杂度：O(1)。

    难点：
    第一，根据上面的操作总结出规律；使用模仿法，一步一步分解开人类的思维，然后转换成算法。
    第二，如何证明这个规律正确。证明所有的情况。
    """

    def IsPopOrder(self, pushV, popV):
        stack = []
        push_index = 0
        target_index = 0
        length = len(pushV)

        while target_index < length:
            if not stack:
                stack.append(pushV[push_index])
                push_index += 1
            else:
                if stack[-1] == popV[target_index]:
                    stack.pop()
                    target_index += 1
                else:
                    # pushV 里没有剩余元素了，不能 push
                    if push_index == length:
                        # 由于也不能 pop，所以不可能
                        return False
                    else:
                        stack.append(pushV[push_index])
                        push_index += 1

        return True
