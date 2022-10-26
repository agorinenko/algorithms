"""
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
"""
from bisect import bisect_left
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for idx, i in enumerate(nums):
            data[i] = idx

        for idx, i in enumerate(nums):
            need_i = target - i
            # Это условие работает с повторами, тк мы записали в таблицу индекс последнего элемента, а идем с начала
            if need_i in data and idx != data[need_i]:
                return [data[need_i], idx]

    def two_sum2(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for idx, i in enumerate(nums):
            need_i = target - i
            # Это будет работать, тк от перемены мест слагаемых сумма не меняется
            if need_i in data:
                return [data[need_i], idx]

            data[i] = idx

    def two_sum1(self, nums: List[int], target: int) -> List[int]:
        # brute force way O(n*2)
        res = []
        for idx, i in enumerate(nums):
            for idx2, j in enumerate(nums):
                if idx != idx2 and i + j == target:
                    return [idx, idx2]

        return res
