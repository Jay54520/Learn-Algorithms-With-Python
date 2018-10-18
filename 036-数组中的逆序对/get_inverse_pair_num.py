# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.pairs = 0

    def InversePairs(self, data):
        """
        在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
        并将P对1000000007取模的结果输出。 即输出P%1000000007。题目保证输入的数组中没有的相同的数字。

        比如 [7, 5, 6, 4] 有 [7, 5], [7, 6], [7, 4], [5, 4], [6, 4] 5 个逆序对。

        算法1：

        遍历数组，取当前数字为 flag
            遍历之后的元素，如果当前数字小于 flag，则逆序对个数加一

        复杂度分析：
        时间复杂度：O(n^2)：(n - 1) + (n - 2) + ... + 1。
        空间复杂度：O(1)

        算法2：
        在 self.InversePairs merge 时，统计逆序对数目。原理是子数组的逆序对数目相加就是整个数组的逆序对数目。并且我们
        通过排序避免了重复统计。

        复杂度分析：
        与 merge_sort 相同。
        时间复杂度：O(nlogn)
        空间复杂度：O(n)
        """
        self._inverse_pairs(data)
        return self.pairs

    def _inverse_pairs(self, data):
        if len(data) <= 1:
            return data
        sorted_data = []
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        left = self._inverse_pairs(left)
        right = self._inverse_pairs(right)
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_data.append(left[left_index])
                left_index += 1
            else:
                sorted_data.append(right[right_index])
                right_index += 1
                # 对于 [5, 7], [4, 6]，5 > 4，所以 5 后面的元素也大于 4
                self.pairs += len(left) - left_index

        if left_index < len(left):
            sorted_data.extend(left[left_index:])
        else:
            sorted_data.extend(right[right_index:])
        return sorted_data

