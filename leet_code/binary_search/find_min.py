from typing import List


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
        else:
            right = mid
    return left


class Solution:
    def findMin(self, nums: List[int]) -> int:
        idx = find_min(nums)
        return nums[idx]
