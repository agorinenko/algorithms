from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(nums) - 1
        while left_ptr < right_ptr:
            s = nums[left_ptr] + nums[right_ptr]
            if s == target:
                return [left_ptr + 1, right_ptr + 1]

            if s < target:
                left_ptr += 1
            else:
                right_ptr -= 1

        return []
