"""
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))