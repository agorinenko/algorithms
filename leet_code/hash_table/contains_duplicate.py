"""
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
"""
from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        data = set()
        for i in nums:
            if i in data:
                return True
            data.add(i)

        return False
