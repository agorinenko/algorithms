from typing import List


def test_1():
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2


def test_2():
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    cnt += 1

            if cnt <= mid:
                left = mid + 1
            else:
                right = mid

        return left

    def findDuplicate_2(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return nums[left]
            right += 1
            left += 1

        raise ValueError

    def findDuplicate_1(self, nums: List[int]) -> int:
        memory = set()
        for num in nums:
            if num in memory:
                return num
            memory.add(num)

        raise ValueError
