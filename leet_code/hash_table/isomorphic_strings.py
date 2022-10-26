"""
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
Объяснение, что такое изоморфная строка
https://codeforces.com/problemset/problem/985/F?locale=ru
"""


class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        data_s = {}
        data_t = {}

        for left, s_char in enumerate(s):
            right = len(s) - 1 - left
            t_char = t[right]
            data_s[s_char] = t[left]
            data_t[t_char] = s[right]

        if len(data_s) != len(data_t):
            return False

        for k, v in data_s.items():
            if data_t[v] != k:
                return False

        return True
