# -*- coding:utf-8 -*-
class Solution:
    
    def __init__(self):
        self.data = []
        self.k = None
    
    def GetNumberOfK(self, data, k):
        """
        统计一个数字在排序数组中出现的次数。
        比如 [1, 2, 3, 3, 3, 3, 4, 5] 中 3 出现了 4 次。

        算法1：
        二分查找 k 在数组中的位置，
        如果没有找到，说明 k 不存在，返回 0；
        如果找到了，由于 k 不一定是在它第一个出现的位置，所以我们向前找，直到遇到
        k - 1 或者到达数组头部；同理，k 不一定是在它最后出现的位置，所以我们向后
        找，直到遇到 k + 1 或者到达数组尾部。

        复杂度分析：
        时间复杂度：二分查找 O(logn)，如果数组中都是相同的数字，那么为 O(n)
        空间复杂度：O(1)

        算法2：
        如果没有找到，说明 k 不存在，返回 0；
        如果找到了，找到 k 第一次和最后一次的索引，那么 k 的数目为两次索引之差加一。
        通过二分查找找到第一个和最后一个位置。
        第一个位置：一直在找到的前半部分数组中寻找，直到到达数组头部或者找不到为止
        最后一个位置：一直在找到的后半部分数组中寻找，直到到达数组尾部或者找不到为止
        复杂度分析：
        时间复杂度：logn + log(n/2) + log(n/4) + ... log(1)，为 O((log n)2)。
        O(log n/2) = O( (log n) + log(1/2))， 1 / 2 相比 n 可以忽略，而一共有 logn 项，
        所以为 O(logn * logn) = O(logn^2)
        空间复杂度：O(1)
        """
        self.data = data
        self.k = k
        k_index = self.binary_search(0, len(data) - 1)
        if k_index is None:
            return 0
        first_k = self.find_first_k(0, k_index)
        last_k = self.find_last_k(len(self.data) - 1, k_index)
        return last_k - first_k + 1

    def binary_search(self, start, end):
        """
        For [0, 0], start is 0, end is 1
        :param start:
        :param end:
        :return:
        """
        if not self.data or start > end:
            return
        mid = (end + start) // 2
        if self.data[mid] == self.k:
            return mid
        elif self.data[mid] > self.k:
            return self.binary_search(start, mid - 1)
        else:
            return self.binary_search(mid + 1, end)

    def find_first_k(self, first_index, k_index):
        before_k_index = self.binary_search(first_index, k_index - 1)
        if before_k_index is None:
            return k_index
        return self.find_first_k(first_index, before_k_index)

    def find_last_k(self, last_index, k_index):
        after_k_index = self.binary_search(k_index + 1, last_index)
        if after_k_index is None:
            return k_index
        return self.find_last_k(last_index, after_k_index)