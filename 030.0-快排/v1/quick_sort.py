# -*- coding: utf-8 -*-

"""
将数组分为 3 部分，[小于 pivot，pivot，大于等于 pivot]。

我们定义 before_pivot_index 为 pivot 前面的那个索引，before_pivot_index 的初始值为 start - 1。

遍历数组，
    如果当前值小于 pivot，根据定义，pivot 应该在 before_pivot_index 后面，
    而 before_pivot_index 现在在当前值的前面，所以当前值会在 pivot 后面，即小于 pivot 的值在 pivot 后面，不符合定义。
    为了符合定义，将 before_pivot_index += 1，然后 swap(before_pivot_index, current_index)

        为什么 before_pivot_index +=1？
        因为遇到了一个比 pivot 更小的元素，而这个元素要位于 pivot 前面。所以把 pivot 挤向后一个位置。

    反之，如果值大于 pivot，那么符合定义，不需要做任何操作。

遍历完成后，将 pivot 移动到 pivot_index 的位置，这样整个数组就变成了 [小于 pivot，pivot，大于等于 pivot]。
然后分别对 pivot 左右两边的数组进行快排，这样左右两边的数组也有序了，所以整个数组就有序了。如果理解有问题，可以
看参考中的视频。

根据上面，算法为：

* 终止条件：数组长度小于 1，即 end <= start，则数组有序的，直接返回
* 循环：对当前数组进行 partition 使其变为 [小于 pivot，pivot，大于等于 pivot] 的数组，并得到 pivot_index，然后对 pivot 两边的数组再进行快排。

复杂度：
* 最差时间复杂度：如果每次循环中，pivot 都是最后一个（最大的），那么就相当于冒泡排序，每次移动最大元素
到它的位置 n + (n - 1) + (n - 2) + ... + 1 = O(n^2)
* 平均时间复杂度：对于随机的数组，pivot 平均会位于中间，那么要操作 2 ^ count = n => count = logn，
而每次总计要移动 n 次，所以为 O(nlogn)
* 空间复杂度：O(1)。对输入进行交换而没有创建额外数组

参考

视频：https://www.youtube.com/watch?v=MZaf_9IZCrc
代码：https://www.geeksforgeeks.org/quick-sort/
"""


def partition(a_list, start, end):
    """对 a_list[start:end+1] 进行 partition"""
    before_pivot_index = start - 1
    pivot_value = a_list[end]
    for current_index in range(start, end):
        if a_list[current_index] < pivot_value:
            before_pivot_index += 1
            a_list[before_pivot_index], a_list[current_index] = a_list[current_index], a_list[before_pivot_index]
    pivot_index = before_pivot_index + 1
    # 没必要先弹出再插入，因为 pivot 后面的值没有顺序关系，只要大于等于 pivot 即可
    a_list[pivot_index], a_list[end] = a_list[end], a_list[pivot_index]
    return pivot_index


def quick_sort(a_list):
    _quick_sort(a_list, 0, len(a_list) - 1)
    return a_list


def _quick_sort(a_list, start, end):
    if end <= start:
        return

    pivot_index = partition(a_list, start, end)
    _quick_sort(a_list, 0, pivot_index - 1)
    _quick_sort(a_list, pivot_index + 1, end)
