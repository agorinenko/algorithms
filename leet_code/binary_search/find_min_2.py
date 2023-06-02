from typing import List


def test_main_1():
    nums = [2, 2, 2, 0, 1]
    assert Solution().findMin(nums) == 0


def test_main_2():
    nums = [3, 3, 1, 3]
    assert Solution().findMin(nums) == 1


def test_main_3():
    nums = [1, 3, 3]
    assert Solution().findMin(nums) == 1


def find_min(arr: list[int]):
    left = 0
    right = len(arr) - 1

    if len(arr) == 1:
        return 0

    if arr[left] < arr[right]:
        return left

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        elif arr[mid] < arr[left]:
            right = mid
        else:
            right -= 1

    return left


class Solution:
    def findMin(self, nums: List[int]) -> int:
        idx = find_min(nums)
        return nums[idx]
