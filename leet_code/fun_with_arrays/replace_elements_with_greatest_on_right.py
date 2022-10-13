"""
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""
from typing import List


class Solution:
    def replace_elements(self, arr: List[int]) -> List[int]:
        for idx in range(len(arr)):
            if idx == len(arr)-1:
                arr[idx] = -1
            else:
                arr[idx] = max(arr[idx+1:])

        return arr
