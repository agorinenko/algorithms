"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
"""
from leet_code.fun_with_arrays.third_max import Solution


def test_main_1():
    nums = [3, 2, 1]
    assert Solution().third_max(nums) == 1


def test_main_2():
    nums = [1, 2]
    assert Solution().third_max(nums) == 2


def test_main_3():
    nums = [2, 2, 3, 1]
    assert Solution().third_max(nums) == 1


def test_main_4():
    nums = [1, 5, 3, 6, 2, 6, 10, 3, 2, 1]
    assert Solution().third_max(nums) == 5
