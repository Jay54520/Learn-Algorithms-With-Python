# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        """ 
        用数字表示一副扑克牌，大\小王是 0 并且可以看成任何数字，并且A看作1，J为11，Q为12，K为13。
        比如输入 [1, 3, 0, 0, 5]，将 0, 0 看做 2 和 4，则可以构成 1~5 的顺子，所以返回 True。

        算法：
        顺子的定义：排序后的数组是这样的：x0, x0 + 1, ... x0 + 4。由于 0 可以当成任意数字，
        所以我们可以用 0 去填补空缺——排序后数组相邻两数字的间隔大小。
        如果 0 的个数大于等于空缺的个数，那么就可以构成顺子；否则，不能构成顺子。
        特殊情况有：如果两个数字相同，那么虽然 gap 为 0，但是也不可能成为顺子，所以直接返回 False，
        并且由于数组是排序好的，所以相同的数字一定相邻。

        * 给数组排序
        * 统计 0 的个数
        * 统计空缺个数
        * 比较 0 的个数和空缺个数，得出结论

        由于个数限定了是 5，所以不需要分析复杂度。
        """
        if not numbers:
            return False

        numbers = list(sorted(numbers))
        zero_count = numbers.count(0)
        # 从零之后开始统计空缺个数，因为 0 是可以变化的
        start_index = zero_count
        gap_count = 0
        for i in range(start_index, len(numbers) - 1):
            if numbers[i + 1] == numbers[i]:
                return False
            gap_count += numbers[i + 1] - numbers[i] - 1
        if zero_count >= gap_count:
            return True
        return False
