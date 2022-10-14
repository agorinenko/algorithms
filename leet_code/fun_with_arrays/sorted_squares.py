"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sequence = [x * x for x in nums]
        return sorted(sequence)