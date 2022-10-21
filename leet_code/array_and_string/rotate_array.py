"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/
https://leetcode.com/problems/rotate-array/discuss/1730142/JavaC%2B%2BPython-A-very-very-well-detailed-explanation
"""
from typing import List


class Solution:
    def reverse(self, nums, l, r):
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)  # if we have let's say 101 to rotate, then we only rotate it 1 time not 101 times

        self.reverse(nums, 0, len(nums) - k - 1)  # part 1 reverse
        self.reverse(nums, len(nums) - k, len(nums) - 1)  # part 2 reverse
        self.reverse(nums, 0, len(nums) - 1)  # complete reverse
