# -*- coding:utf-8 -*-

class Solution:
    def replaceSpace(self, s):
        """
        请实现一个函数，将一个字符串中的每个空格替换成“%20”。
        例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

        对于 Python 来说，自带的特性已经处理了这个问题，如果面试官同意的话，就使用它。
        如果面试官不同意，那我们继续思考。

        算法及证明

            遍历字符串，
            如果不是空格，那么将该字符串直接加入结果
            否则，将 %20 加入结果。

            由于是遍历操作，所以处理了字符串为空的边界情况。

        复杂度分析

            时间复杂度：遍历一遍，为 O(n)
            空间复杂度：O(n)。假设原字符串是 n 个空格，那么新字符串的长度为 3n，O(3n) = O(n)。

            自带的为 O(m*n)，m 是子字符串的长度，这里是 1，所以与自带的 replace 的复杂度相同。

        :param s: 原字符串
        :return:
        """
        replaced_string = ''

        for raw_s in s:
            if raw_s == ' ':
                replaced_string += '%20'
            else:
                replaced_string += raw_s

        return replaced_string