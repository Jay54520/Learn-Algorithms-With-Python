# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        """
        翻转句子中单词的顺序，但单词内字符的顺序不变。标点符号和普通字母一样处理。
        例如输入“I am a student”，则输出 “student. a am I”。

        算法1：
        我们认为句子是以空格分隔的多个字符，所以先以空格进行 split，再调用自带的 reversed 对其翻转，
        然后再以空格聚合成字符串。

        复杂度分析：
        时间复杂度：O(n)
        空间复杂度：O(n)。s.split 会产生一个大小为 n 的列表。
        """
        return ' '.join(reversed(s.split(' ')))