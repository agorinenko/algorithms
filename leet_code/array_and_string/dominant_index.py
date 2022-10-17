"""
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
"""
from typing import List


class Solution:
    def dominant_index(self, nums: List[int]) -> int:
        max_idx = 0
        for idx in range(1, len(nums)):
            if nums[idx] > nums[max_idx]:
                max_idx = idx

        for idx in range(0, len(nums)):
            if idx != max_idx and nums[max_idx] < 2 * nums[idx]:
                return -1

        return max_idx
