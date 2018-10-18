# -*- coding: utf-8 -*-


def merge_sort(a_list, cmp):
    """
    如果一个数组为空或者只有一个元素，那么它就是有序的，直接返回它们本身。
    如果数组的长度大于 1，那么它可能是无序的，于是将其均匀拆分成两个数组，然后再对这两个数组
    调用 merge_sort。那么这个两个数组现在是有序的了，如果 merge_sort 的实现是正确的。
    然后合并两个有序的子数组，然后返回合并后的数组。
    同时从头开始遍历两个数组：
        * 如果左右数组都不为空。根据 cmp()，获取排序在前面的元素，并将其加入到 sorted_list，然后对选出元素的数组索引加 1
        * 如果一个数组之后的元素为空，就将另一个数组（这个数组已经是有序的了）加入到 sorted_list，然后返回 sorted_list
            * 如果左数组为空，那么将右数组加入到 sorted_list
            * 如果右数组为空，那么将左数组加入到 sorted_list
        如何判断数组为空？如果遍历的数组索引小于数组的长度，则数组不为空。比如数组长度是 0，由于不可能有比 0 更小的索引，所以此时为空；
        如果数组长度为 1，那么当索引为 0 时不为空，为 1 时为空。

    复杂度分析：
    时间复杂度：把 n 个元素分成 n 份需要 logn 次，然后每次都要聚合出一个有序的数组，所以为 O(nlogn)
    空间复杂度：O(n)。用于存放 sorted_list
    """
    if len(a_list) <= 1:
        return a_list
    sorted_list = []
    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]
    left = merge_sort(left, cmp)
    right = merge_sort(right, cmp)
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if cmp(left[left_index], right[right_index]):
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        sorted_list.extend(left[left_index:])
    else:
        sorted_list.extend(right[right_index:])
    return sorted_list

