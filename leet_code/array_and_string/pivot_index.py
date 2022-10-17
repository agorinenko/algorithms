"""
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
"""
from typing import List


class Solution:
    def pivot_index(self, nums: List[int]) -> int:
        sum_left = []
        for idx in range(len(nums)):
            if idx == 0:
                sum_left.append(nums[idx])
            else:
                sum_left.append(sum_left[-1] + nums[idx])

        sum_right = []
        for idx in range(len(nums) - 1, -1, -1):
            if idx == len(nums) - 1:
                sum_right.append(nums[idx])
            else:
                sum_right.append(sum_right[-1] + nums[idx])
                
        sum_right.reverse()

        for idx in range(len(nums)):
            if sum_left[idx] == sum_right[idx]:
                return idx

        return -1
