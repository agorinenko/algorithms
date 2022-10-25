"""
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/
"""
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        data = set()
        for i in nums:
            if i in data:
                data.remove(i)
            else:
                data.add(i)
        x = next(iter(data))
        return x