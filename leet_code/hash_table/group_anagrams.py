"""
https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/
"""
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in data:
                data[key].append(s)
            else:
                data[key] = [s]

        return list(data.values())
