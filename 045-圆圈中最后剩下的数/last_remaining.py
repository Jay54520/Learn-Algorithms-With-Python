# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        """
        首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
        每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
        从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,
        可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
        请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

        将上面抽象为：
        0 ~ (n - 1) 这 n 个数字排成一个圆圈，从数字 0 开始每次从这个圆圈
        里删除第 m 个数字。求圆圈里最后剩下的数字。当 n、m 都等于 0 时，返回 -1。

        比如 0->1->2->3->4
            ↑            ↓
             <-----------
        当 m = 3 时，删除的前 4 个数字是 2、0、4、1。

        算法1：
        使用数组模拟环，我们将数组的最后一个索引看成是第一个索引。第 m 个数字相当于 (当前索引 + m - 1) % 当前数组长度

        如果数组中含有多于 1 个元素，则一直删除当前索引后的第 m 个，删除之后当前的索引
        就还是停留在对应的位置，符合题目要求。
        跳出（while 长度大于 1）的循环后，数组中只剩下一个元素，即为结果。

        复杂度分析：
        时间复杂度：O(n^2)。pop() 操作：n + n - 1 + ... + 1 = O(n^2)
        空间复杂度：O(n)。用于储存的数组。
        """
        if m == 0 and n == 0:
            return -1

        nums = list(range(n))
        i = 0
        while len(nums) > 1:
            i = (i + m - 1) % len(nums)
            nums.pop(i)
        return nums[0]
