# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        数组中可能有一个数字出现的次数**超过**数组长度的一半，如果
        有则返回这个数字，否则返回 0。所以 0 不可能在数组中出现
        超过一半。

        例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
        由于数字2在数组中出现了5次，超过数组长度的一半，
        因此输出2。如果不存在则输出0。

        算法及证明：

        算法1：

        如果数组为空，返回 0；
        如果数组只有一个数字，返回这个数字；
        如果数组有两个数字，那么只有当大于 2 // 2 = 1时，即所有数字相同时才可能；
        如果有三个数字，那么要大于 3 // 2 = 1

        把数组从中间分成两份，那么这个数字一定在两边都存在。对两边求交集，
        然后检验交集数字的次数。求交集的时间复杂度为 O(n ^ 2)，所以不用这个方法。

        算法2：

        维护一个字典，记录所有元素的出现次数，当发现大于一半的次数时，返回；
        如果遍历完成后都没有发现，说明不存在。

        时间复杂度：O(n)
        空间复杂度：O(n)

        算法3：

        假如这个数字存在，那么这个数字与其他数字抵消后，最后剩下的一定是这个
        数字。是充分不必要条件。因为 [1, 2, 1, 2, 3] 中的 3 也满足这个条件
        但不是超过一半的数字。所以再遍历一次数组，统计剩下的数字出现次数，然后
        判断是否满足要求。

        时间复杂度：O(n)
        空间复杂度：O(1)

        抵消算法

        遍历数组，将第一个数字加入次数字典中，次数为 1。如果后一个是相同的数字，
        那么给次数加一，否则减一。如果次数为 0，则将其移除数组。
        """
        times = self.generate_times(numbers)
        if not times:
            return 0
        number = times.keys()[0]
        half_length = len(numbers) // 2
        number_count = self.count_number(number, numbers)
        if number_count > half_length:
            return number
        else:
            return 0

    def generate_times(self, numbers):
        """根据 numbers 生成次数字典"""
        times = {}
        for number in numbers:
            if not times:
                times[number] = 1
            else:
                if number in times:
                    times[number] += 1
                else:
                    key = times.keys()[0]
                    times[key] -= 1
                    if times[key] == 0:
                        del times[key]
        return times

    def count_number(self, number, numbers):
        number_count = 0
        for n in numbers:
            if n == number:
                number_count += 1
        return number_count
