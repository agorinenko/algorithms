"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
"""
from typing import List


class Solution:
    def array_pair_sum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for idx in range(int(len(nums) / 2)):
            res += min(nums[idx * 2], nums[idx * 2 + 1])

        return res
