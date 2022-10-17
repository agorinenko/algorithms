"""
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
"""
from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        res = list(str(int(''.join([str(i) for i in digits])) + 1))
        return [int(i) for i in res]