"""
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
"""
from typing import List


class Solution:
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        data = {}
        for idx, i in enumerate(nums):
            if i in data:
                data[i].append(idx)
            else:
                data[i] = [idx]

        uniq_items = set(nums)
        for i in uniq_items:
            for pointer_1 in range(len(data[i])):
                for pointer_2 in range(pointer_1 + 1, len(data[i])):
                    if abs(data[i][pointer_1] - data[i][pointer_2]) <= k:
                        return True

        return False
