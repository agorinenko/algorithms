"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
"""
from typing import List


class Solution:
    def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
        all_nums = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in all_nums:
                result.append(i)

        return result
