# -*- coding:utf-8 -*-
from collections import OrderedDict

NOT_FOUND = -1


class Solution:
    def FirstNotRepeatingChar(self, s):
        """
        在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
        并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

        ## 算法1

        遍历字符串，将字符加入 OrderedDict，字典的值为 [times, first_index]：
            * 如果不存在，设置为 0
            * 否则，+= 1
        遍历结束后，遍历字典，并返回第一个出现次数为 1 的字符的索引；如果遍历完字典后都没有，返回 -1

        复杂度分析：
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        char_times = OrderedDict()
        for index, char in enumerate(s):
            if char_times.get(char):
                times_first_index = char_times[char]
                times_first_index[0] += 1
            else:
                char_times[char] = [1, index]
        for char, times_first_index in char_times.items():
            if times_first_index[0] == 1:
                return times_first_index[1]
        return NOT_FOUND
