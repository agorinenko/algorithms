"""
https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra
memory.
"""
from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        k = 0

        for idx in range(len(nums)):
            p = idx - k
            if nums[p] == val:
                for i in range(p + 1, len(nums)):
                    nums[i - 1] = nums[i]

                nums[len(nums) - 1] = 0
                k += 1

        return len(nums) - k
