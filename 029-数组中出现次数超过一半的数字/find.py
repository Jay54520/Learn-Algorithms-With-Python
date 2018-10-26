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

        假设这样的数字存在，那么进行抵消后剩下的数字就会是它；
        如果这样的数字不存在，进行抵消后也可能会剩下数字。比如 [1, 2, 1, 2, 3]

        所以抵消后，如果没有剩下数字，返回 0；
        如果剩下数字，统计该数字的出现次数，如果大于一半，返回它；否则，返回 0。

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        res = 0
        times = {}
        for n in numbers:
            if times:
                original_key = list(times.keys())[0]
                if n == original_key:
                    times[original_key] += 1
                else:
                    times[original_key] -= 1
                    if times[original_key] == 0:
                        del times[original_key]
            else:
                times[n] = 1
        if times:
            tmp_res = list(times.keys())[0]
            if numbers.count(tmp_res) > len(numbers) // 2:
                res = tmp_res
        return res
