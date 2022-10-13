"""
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        override_pointer = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[override_pointer] = nums[idx]
                override_pointer += 1

        for idx in range(override_pointer, len(nums)):
            nums[idx] = 0

