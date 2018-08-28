# -*- coding:utf-8 -*-

from heapq import _siftdown_max, _siftup_max


def heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup_max(heap, 0)
        return returnitem
    return lastelt


def heapreplace_max(heap, item):
    """Maxheap version of a heappop followed by a heappush."""
    returnitem = heap[0]  # raises appropriate IndexError if heap is empty
    heap[0] = item
    _siftup_max(heap, 0)
    return returnitem


def heappush_max(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown_max(heap, 0, len(heap) - 1)


def heappushpop_max(heap, item):
    """Fast version of a heappush followed by a heappop."""
    if heap and heap[0] > item:
        # if item >= heap[0], it will be popped immediately after pushed
        item, heap[0] = heap[0], item
        _siftup_max(heap, 0)
    return item


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
        输入n个整数，找出其中最小的K个数。
        例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

        算法1：

        排序后取出前 k 个数。

        复杂度：
        时间复杂度：O(nlogn)
        空间复杂度：O(n)

        算法2：

        将所有数字构成最小堆，然后 pop() k 次取出前 k 个数。

        复杂度：
        时间复杂度：构建最小堆 —— O(n)，然后取出前 k 个数 —— O(klogn)，所以为 max(O(n), O(klogn))
        空间复杂度：O(n)

        算法2优化：

        构建节点数量为 k 的最大堆。在节点数量要超过 k 时：

            * 如果新元素大于等于最大元素，跳过；
            * 如果新元素小于最大元素，剔除最大元素，加入新元素

        遍历完成后剩下的就是 k 个最小的数字。所以关于取 k 个数的算法，复杂度中一定要包含 k，
        否则 k = 1 会和 k = n 的复杂度一样。

        复杂度：
        时间复杂度：遍历数组 —— O(n)，每次 O(logk)，所以为 O(nlogk)
        空间复杂度：O(k)

        这里优化的原因是，当 k 小于 n 时，排序算法多计算了 (k, n)。这样的“最”问题就可以用堆解决。

        Python 有 heapq 库实现了堆。根据 heapq 的文档，实现的是最小堆，并且没有找到参数可以调节它。
        有人推荐的方法有：

        * 传入堆的值取负数，取出来再取负数
        * 创建一个类，使大于、小于相反

        我认为这样会增加不必要的时间复杂度，为什么不根据 Python 的源码实现一个最大堆呢？
        找到了 https://github.com/he-zhe/heapq_max/blob/master/heapq_max/heapq_max.py

        边界条件：

        * k 可以是任意整数
            * k <= 0，返回 []
            * 0 < k <= length，返回 [:k]
            * > length，牛客网测试用例要求返回 []
        * tinput 可以含有任意个数元素，如果为 []，返回 []
        """
        if k > len(tinput):
            return []
        elif k <= 0:
            return []
        if len(tinput) == 0:
            return []

        heap_max = []

        for num in tinput:
            if len(heap_max) == k:
                maximum = heap_max[0]
                if num >= maximum:
                    continue
                else:
                    heappushpop_max(heap_max, num)
            else:
                heappush_max(heap_max, num)

        return list(sorted(heap_max))
