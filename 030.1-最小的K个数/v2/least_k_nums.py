# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
        输入n个整数，找出其中最小的K个数。
        例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

        算法4：

        使得比第 k 个数字小的都位于数组左边，反之位于右边。这样结果可能是无序的，
        但题目也没有要求有序，虽然示例的返回是有序的。

        在 Partition 算法中，如果 pivot_index 大于 k - 1，那么说明目标在 pivot_index 左边；
        否则，目标在 pivot_index 右边。

        最差时间复杂度：O(n^2)，partition 退化为冒泡排序
        平均时间复杂度：O(nlogn)
        空间复杂度：O(1)

        缺点：

        * 要修改输入数据
        * 如果输入数据很大（大于内存），就不能使用

        所以面试时可以询问面试官输入参数是否要满足上述两个情况。
        """
        if k > len(tinput):
            return []
        elif k <= 0:
            return []
        if len(tinput) == 0:
            return []

        start = 0
        end = len(tinput) - 1
        pivot_index = self.partition(tinput, 0, end)
        # 由于 k 最大为 length，所以 pivot_index 最大为 k - 1
        while pivot_index != k - 1:
            if pivot_index > k - 1:
                end = pivot_index - 1
                pivot_index = self.partition(tinput, start, end)
            else:
                start = pivot_index + 1
                pivot_index = self.partition(tinput, start, end)

        # 牛客网的测试判例是要求有序
        return list(sorted(tinput[:k]))

    def partition(self, a_list, start, end):
        """对 a_list[start:end+1] 进行 partition，与 quick_sort 中的相同"""
        before_pivot_index = start - 1
        pivot_value = a_list[end]
        for current_index in range(start, end):
            if a_list[current_index] < pivot_value:
                before_pivot_index += 1
                a_list[before_pivot_index], a_list[current_index] = a_list[current_index], a_list[before_pivot_index]
        pivot_index = before_pivot_index + 1
        # 没必要先弹出再插入，因为 pivot 后面的值没有顺序关系
        a_list[pivot_index], a_list[end] = a_list[end], a_list[pivot_index]
        return pivot_index
