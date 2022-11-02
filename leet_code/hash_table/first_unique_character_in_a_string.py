"""
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
"""


class Solution:
    def first_uniq_char(self, s: str) -> int:
        data = {}
        for i in s:
            if i in data:
                data[i] = data[i] + 1
            else:
                data[i] = 1

        for idx, i in enumerate(s):
            if 1 == data[i]:
                return idx

        return -1
