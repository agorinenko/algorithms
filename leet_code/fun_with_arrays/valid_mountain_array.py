"""
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""
from typing import List


class Solution:
    def valid_mountain_array(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        max_item = arr[0]
        down = arr[0] > arr[1]

        for idx in range(1, len(arr)):
            if arr[idx] == arr[idx - 1]:
                return False

            if down and arr[idx] > arr[idx - 1]:
                return False

            if arr[idx] > max_item:
                # up
                max_item = arr[idx]
                down = False
            else:
                # down
                down = True

        is_mountain = arr[0] < max_item and max_item > arr[len(arr) - 1]

        return is_mountain
