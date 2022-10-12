"""
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
"""

from typing import List


class Solution:
    def check_if_exist(self, arr: List[int]) -> bool:
        table = set()
        for idx in range(len(arr)):
            if arr[idx] * 2 in table or arr[idx] / 2 in table:
                return True
            table.add(arr[idx])

        return False