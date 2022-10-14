"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].
"""
from typing import List


class Solution:
    def height_checker(self, heights: List[int]) -> int:
        valid_array = sorted(heights)
        i = 0
        for idx in range(len(heights)):
            if heights[idx] != valid_array[idx]:
                i += 1
        return i
