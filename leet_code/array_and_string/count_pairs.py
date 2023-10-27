from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c = 0
        for i, val_i in enumerate(nums):
            for j, val_j in enumerate(nums[i + 1:]):
                if val_i + val_j < target:
                    c += 1
        return c
