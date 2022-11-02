"""
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1134/
"""
from typing import List


class Solution:
    def four_sum_count(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums1 = {}
        for n1 in nums1:
            for n2 in nums4:
                s = n1 + n2
                if s in sums1:
                    sums1[s] += 1
                else:
                    sums1[s] = 1

        counter = 0
        for n3 in nums3:
            for n4 in nums2:
                s = 0 - (n3 + n4)
                if s in sums1:
                    counter += sums1[s]

        return counter
