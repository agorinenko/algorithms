"""
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
"""
from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        prefix = ''
        for c in strs[0]:
            candidate = prefix + c
            status = []
            for s in strs[1:]:
                status.append(s.startswith(candidate))

            if all(status):
                prefix = candidate
            else:
                return prefix

        return prefix
