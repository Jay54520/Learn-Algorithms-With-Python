# -*- coding: utf-8 -*-

"""
* 终止条件：数组长度小于 1，则是有序的，不需要进行任何操作，直接返回
* 循环：使当前数组变为 [<pivot, pivot, >=pivot] 的数组，然后对 pivot 两边的数组进行快排。
使用索引区分数组范围。

复杂度：
* 平均时间复杂度：对于随机的数组，pivot 平均会位于中间，那么要操作 2 ^ count = n => count = logn，
而每次总计要移动 n 次，所以为 O(nlogn)。相比 v1，增加了连接 list 的操作。平均为 n / 2，因为左右两边
平均为 n / 2 - 1 个元素。所以为 n / 2 + n / 4 + ... + 1 = (n / 2 + 1) * logn = O(nlogn)
所以不影响总的时间复杂度。但代码简化了很多，可读性也高了很多。
* 空间复杂度：O(1)。没有创建额外数组，因为新的 list 只是对旧有 list 元素的引用而没有新建
"""


def quick_sort(a_list):
    if len(a_list) > 1:
        # 注意所有的返回 list 类型
        pivot = a_list[0]
        return quick_sort([x for x in a_list if x < pivot]) + \
               [pivot] + quick_sort([x for x in a_list if x > pivot])
    else:
        return a_list
