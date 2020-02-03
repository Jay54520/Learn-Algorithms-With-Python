# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        """
        loop [2, 1, 3, 4, 5]
        if current element is odd:
            * 2
            * 1
                exchange with 1st element when 1st element is even
                [1, 2, 3, 4, 5]
            * 3
               exchange with latest element whose prior element is odd
               [1, 3, 2, 4, 5]
            * 5
               if we do as above, we will get [1, 3, 5, 4, 2] that will break the
               relative order.
               we should delete it and insert instead exchange directly.
        """
        for index, element in enumerate(array):
            if element % 2 != 0:
                inserted_index = index
                for j in range(inserted_index - 1, -1, -1):
                    if array[j] % 2 != 0:
                        inserted_index = j + 1
                        break
                    elif j == 0:
                        inserted_index = 0
                if inserted_index != index:
                    self._insert(array, index, inserted_index)
        return array

    def _insert(self, array, index, inserted_index):
        """
        exchange index with index - 1 until index == inserted_index
        [1, 2, 3, 4]
            1     3
        [1, 2, 4, 3]
            1  2
        [1, 4, 2, 3]
            1

        [1, 3, 2, 4, 5, 6]
               2     4
        [1, 3, 2, 5, 4, 6]
               2  3
        [1, 3, 5, 2, 4, 6]
               2 2
        """
        while index > inserted_index:
            array[index], array[index-1] = array[index-1], array[index]
            index -= 1
