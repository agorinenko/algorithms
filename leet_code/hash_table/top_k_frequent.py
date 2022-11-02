"""
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = counter.most_common(k)
        return [i[0] for i in res]
