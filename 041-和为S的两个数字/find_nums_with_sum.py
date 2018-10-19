# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        """
        输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
        如果有多对数字的和等于S，输出两个数的乘积最小的。

        两个数字相差越大，乘积越小，证明如下：
        设一个数为 x，则另一个为 x + d，d > 0。
        则 2x + d = C => x = (C - d) / 2, y = (C + d) / 2
        则 x * y = (C-d)(C+d)/4=(C^2-d^2)/4 = 一个常数 - d^2/4，所以 d 越大，x * y 越小。

        设两个头尾两个指针i和j，
        如果 i >= j，说明没有找到，返回空
        如果 ai + aj == sum，则答案就是这两个
        如果 ai + aj > sum，将 j 向前移动。不能将 i 向前移动，
            1. 如果 i 是第一个位置（数组边界），显然不能向前移动
            2. 如果 i 不是第一个位置，那么说明经历过了下面的情况，而下面的情况是不符合要求的
        否则，ai + aj < sum，将 i 向后移动。j 不能向后移动：
            1. 如果 j 是最后一个位置（数组边界），显然不能向后移动
            2. 如果 j 不是第一个位置，那么说明经历过了上面的情况，而上面的情况是不符合要求的
        """
        i = 0
        j = len(array) - 1
        while i < j:
            current_sum = array[i] + array[j]
            if current_sum == tsum:
                return [array[i], array[j]]
            elif current_sum > tsum:
                j -= 1
            else:
                i += 1
        return []