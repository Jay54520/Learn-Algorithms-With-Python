# -*- coding:utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, target, array):
        """
        在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

        算法及证明

            取右上角的数字，以下将其称为当前数字
                如果目标数字等于当前数字，返回 true
                如果目标数字大于当前数字，
                    * 由于每行递增、当前数字是所在行的最后一个数字，所以当前数字是所在行最大的数字，所以在当前行不可能存在
                    比当前数字更大的数字，所以目标数字在当前行不存在
                    * 对于当前行下面的任意一行，如果该行的第一个数字大于当前数字，由于每一行是从左到右递增，
                    所以这个行的所有数字都大于右上角数字，所以目标数字只可能存在于当前行下面的数组中。
                如果目标数字小于当前数字，与上面类似，目标数字只可能存在于当前列前面的数组中。

            终止条件：找到目标数字或者找遍了整个数组（下一行或列越界）

        为了不占用额外的空间，使用索引来标记被查找数组的范围而不是创建新的数组。

        复杂度分析：

            时间复杂度：根据上面的算法，每次可以过滤掉一行或一列，所以最大操作数为 row_num + column_num，
            所以时间复杂度为 O(row_num + column_num)，对应的情况为从数组的右上角查找到左下角。

            空间复杂度：由于使用索引来标记被查找数组的范围，没有创建额外的子数组，所以为 O(1)

        思路分析：

            我认为这题利用了边界（右上角）条件对查找范围进行了限制，所以可以逆序思考以及从规律的边界开始考虑。

        :param target: 目标数字
        :param array: 二维数组
        :return: bool 目标数字是否存在
        """
        if not array:
            return False

        # 通过起始行索引和结束列索引描述被查找数组的范围
        start_row_index = 0
        end_column_index = len(array[0]) - 1

        while (start_row_index < len(array)) and (end_column_index >= 0):
            # 右上角元素为第 start_row_index 行、第 end_column_index 个元素
            right_most_num = array[start_row_index][end_column_index]
            if target == right_most_num:
                return True
            elif target > right_most_num:
                start_row_index += 1
            else:
                end_column_index -= 1

        return False
