"""
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1178/
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        data = {}
        for i in nums1:
            if i in data:
                data[i] = [data[i][0] + 1, data[i][1]]
            else:
                data[i] = [1, 0]

        for i in nums2:
            if i in data:
                data[i] = [data[i][0], data[i][1] + 1]
            else:
                data[i] = [0, 1]

        result = []
        for num, cell in data.items():
            count = min(cell[0], cell[1])
            if count >= 1:
                result.extend([num] * count)
        return result
