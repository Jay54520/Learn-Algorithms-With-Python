# -*- coding:utf-8 -*-


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        """
        数组的旋转：rotate the array to the right by k steps, where k is non-negative。 输入一个非递减排序的数组的一个旋转，
        输出旋转数组的最小元素。
        例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转（旋转了 3 次），该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

        算法分析及证明

        观察 [3,4,5,1,2] 可以发现，数组分为了两个非递减的子数组。假设数组旋转了 k(k>=0) 次，那么最大值的索引为 k - 1，
        最小值的索引为 k 并且 array[:k] 和 array[k:] 为两个非递减数组，当 k = 0 时，这两个数组相同。
        并且，旋转前的索引 = 旋转后的索引 % n - k（n 是数组的长度）。

        如果我们以 p1、p2 分别指向第一和第二个数组，middle = (p1 + p2) / 2，如果 array[middle] >= array[p1]，
        那么在原数组中 middle 对应的元素一定在 p1 对应的元素后面，所以 (p1 % n - k) 到 (middle % n - k) 是非递减的：
        array[p1 % n - k] <= array[p1 % n - k + 1] <= ... <= array[middle % n - 1] <= array[middle % n - k] =>
        array[p1 % n] <= array[p1 % n + 1] <= ... <= array[middle % n - 1] <= array[middle % n]  =>
        array[p1] <= array[p1 + 1] <= ... <= array[middle - 1] <= array[middle]
        所以 p1 到 middle 也是非递减的，所以 middle 和 p1 都在第一个非递减数组中；否则，middle 位于第二个数组。

        如果 middle 位于第一个数组，那么将 p1 指向 middle，否则将 p2 指向 middle。 就这样一直缩小 p1、p2 的差距，
        直到 p1、p2 相邻：

        如果此时 array[p1] > array[p2]，那么此时的 p2 就指向第二个数组的第一个元素，也就是最小值。
        否则，说明整个数组只有一个非递减数组——旋转后的数组与原数组相同，此时最小值就是旋转后数组的第一个元素。

        特殊情况是只有一个元素，那么将 p1、p2 相邻扩大为相差小于等于 1；
        没有元素，按照题意返回 0；

        复杂度分析：

        时间复杂度：二分查找，O(logn)
        空间复杂度：O(1)

        评注

        很多视频、解法都没有进行证明，而是直接说结论。

        k 的思路来自：https://www.youtube.com/watch?v=E-p_o_w4GRk
        两个递增数组、middle 的思路来自原书。

        :param rotateArray: :type: list 旋转后的数组
        :return: 数组的最小值
        """
        if not rotateArray:
            return 0

        p1 = 0
        p2 = len(rotateArray) - 1
        middle = (p1 + p2) // 2
        while (p2 - p1) > 1:
            if rotateArray[middle] >= rotateArray[p1]:
                p1 = middle
            else:
                p2 = middle
            middle = (p1 + p2) // 2

        if rotateArray[p1] > rotateArray[p2]:
            return rotateArray[p2]
        else:
            return rotateArray[0]