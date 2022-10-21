"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
"""
import bisect
import math
from typing import List


class Solution:
    def min_sub_array_len2(self, target: int, nums: List[int]) -> int:
        p1 = 0
        p2 = 0

        total = 0
        ans = math.inf

        while p2 < len(nums):
            total = total + nums[p2]
            if total < target:
                p2 += 1
            else:
                ans = min(ans, p2 - p1 + 1)
                total = total - nums[p1] - nums[p2]
                p1 += 1

        return ans if ans != math.inf else 0

    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = math.inf
        # size = len(nums)+1 for easier calculations
        # sums[0]=0 : Meaning that it is the sum of first 0 elements
        # sums[1]=A[0] : Sum of first 1 elements
        sums = [i for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        for i in range(1, len(nums) + 1):
            to_find = target + sums[i - 1]
            bound = bisect.bisect_left(sums, to_find)
            if bound != sums[len(sums) - 1]:
                ans = min(ans, (bound - (sums[0] + i - 1)))
        return ans

    def min_sub_array_len1(self, target: int, nums: List[int]) -> int:
        """
        Approach #1 Brute force [Time Limit Exceeded]
        """
        ans = math.inf
        if len(nums) == 0:
            return 0

        sums = [nums[0]]
        for idx in range(1, len(nums)):
            sums.append(sums[idx - 1] + nums[idx])

        for idx in range(len(nums)):
            for idx2 in range(idx, len(nums)):
                sub_array_sum = sums[idx2] - sums[idx] + nums[idx]

                if sub_array_sum >= target:
                    ans = min(ans, (idx2 - idx + 1))
                    break

        return ans if ans != math.inf else 0
