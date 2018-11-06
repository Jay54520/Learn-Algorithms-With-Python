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
        如果 left >= right，说明没有找到，返回空
        如果 a[left] + a[right] == sum，则答案就是这两个

        我们设定 left 只能向后移动，right 只能向前移动。
        如果 a[left] + a[right] > sum，将 right 向前移动：
            1. 如果 left 是第一个位置（数组边界），显然不能向前移动，与假设符合
            2. 如果 left 不是第一个位置，根据假设，a[left-1] + a[right] < sum，因为只有这种情况 left 才会向后移动。
            所以 left 不能向前移动，只有 right 才能向前移动

        否则，a[left] + a[right] < sum，将 left 向后移动：
            1. 如果 right 是最后一个位置（数组边界），显然不能向后移动
            2. 如果 right 不是第一个位置，根据假设 a[left] + a[right+1] > sum，因为只有这种情况 right 才会向前移动。
            所以 right 不能向后移动，只有 left 才能向后移动
        """
        left = 0
        right = len(array) - 1
        while left < right:
            current_sum = array[left] + array[right]
            if current_sum == tsum:
                return [array[left], array[right]]
            elif current_sum > tsum:
                right -= 1
            else:
                left += 1
        return []