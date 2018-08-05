# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        """
        输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
        所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

        输入 1 2 3 4 5
        输出 1 3 5 2 4

        算法1：

        遍历数组，如果是奇数，加入奇数数组，如果是偶数，加入偶数数组。
        遍历完成后，拼接奇数数组和偶数数组，然后返回。

        复杂度分析：

        时间复杂度：遍历一次的操作数为 n、拼接一次的操作数为 n，所以操作数为 2n，复杂度为 O(n)
        空间复杂度：储存的数组大小总和为 n，所以为 O(n)
        """
        odd_array = []
        even_array = []
        for n in array:
            if n % 2 == 0:
                even_array.append(n)
            else:
                odd_array.append(n)
        return odd_array + even_array