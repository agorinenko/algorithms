"""
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""
from typing import List


class Solution:
    def sort_array_by_parity(self, nums: List[int]) -> List[int]:
        arr = []
        for idx in range(len(nums)):
            if nums[idx] % 2 == 0:
                arr.append(nums[idx])

        for idx in range(len(nums)):
            if nums[idx] % 2 != 0:
                arr.append(nums[idx])

        return arr
