# -*- coding:utf-8 -*-
class Solution:
    def FindNumsAppearOnce(self, array):
        """
        一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。
        返回这两个只出现一次的数字。返回形式：[a,b]。

        比如 [2, 4, 3, 6, 3, 2, 5, 5] 中只有 4, 6 只出现了一次，所以返回 [4, 6]。

        算法1：
        遍历数组，构建一个出现次数的字典，如果在字典中存在则加 1，否则，设置为 1。
        遍历出现次数字典，寻找这两个出现次数为 1 的数字。由于和出现顺序有关，所以要用
        有序字典。
        复杂度分析：
        时间复杂度：O(n)
        空间复杂度：O(n)

        算法2：
        异或的性质：x xor x = 0，0 xor x = x（xor 表示异或）
        如果数组中只有一个数字出现了一次，其他都是偶数次，那么数组中的所有数字进行异或后，结果就是
        那个只出现一次的数字。
        然而题目中有两个数字，所以我们要将这两个数字分割到两个不同的数组中。对于数组中的所有数字进行异或后，
        结果是这两个数字的异或结果。由于这两个数字不同，所以异或结果必定存在 1。将数组根据第一个 1 的出现
        分割成两类，这两类的异或结果就是 a 和 b。
        返回的 [a, b] 应该还与出现顺序有关，所以要根据 a, b 的顺序返回不同的结果。

        复杂度分析：
        时间复杂度：O(n)
        空间复杂度：O(1)

        一般出现偶数次数的，都要用到抵消的思路。这里通过 xor 进行抵消。
        """
        if not array:
            return []
        xor_result = 0
        for e in array:
            xor_result ^= e
        index_of_1 = 0
        while (xor_result & 1) == 0:
            index_of_1 += 1
            xor_result >>= 1
        a, b = 0, 0
        for e in array:
            if self.is_bit(e, index_of_1):
                a ^= e
            else:
                b ^= e
        if array.index(a) < array.index(b):
            return [a, b]
        else:
            return [b, a]

    def is_bit(self, num, index_of_1):
        """num 的 index_of_1 是不是 1"""
        num >>= index_of_1
        return num & 1
