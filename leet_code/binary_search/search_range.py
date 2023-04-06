from typing import List


def left_binary_search(left: int, right: int, check, *args) -> int:
    while left < right:
        mid = (left + right) // 2
        if check(mid, *args):
            right = mid
        else:
            left = mid + 1

    return left


def right_binary_search(left: int, right: int, check, *args) -> int:
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, *args):
            left = mid
        else:
            right = mid - 1

    return left


def search_range(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]

    left, right = 0, len(nums) - 1

    def find_left_target(mid):
        return nums[mid] >= target

    def find_right_target(mid):
        return nums[mid] <= target

    left_idx = left_binary_search(left, right, find_left_target)

    if nums[left_idx] != target:
        left_idx = -1

    right_idx = right_binary_search(left, right, find_right_target)

    if nums[right_idx] != target:
        right_idx = -1

    return [left_idx, right_idx]


def test_search_range():
    nums = [5, 7, 7, 8, 8, 10]
    assert search_range(nums, 8) == [3, 4]


def test_main_2():
    nums = [5, 7, 7, 8, 8, 10]
    assert Solution().searchRange(nums, 6) == [-1, -1]


def test_main_3():
    nums = [1]
    assert Solution().searchRange(nums, 1) == [0, 0]


def test_main_4():
    nums = []
    assert Solution().searchRange(nums, 1) == [-1, -1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1

        def find_left_target(mid):
            return nums[mid] >= target

        def find_right_target(mid):
            return nums[mid] <= target

        left_idx = left_binary_search(left, right, find_left_target)

        if nums[left_idx] != target:
            left_idx = -1

        right_idx = right_binary_search(left, right, find_right_target)

        if nums[right_idx] != target:
            right_idx = -1

        return [left_idx, right_idx]
