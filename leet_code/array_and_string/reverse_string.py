"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/

https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
"""
from typing import List


class Solution:
    def reverse_words(self, s: str) -> str:
        def _reverse_string(s: List[str]) -> str:
            i = 0
            j = len(s) - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            return ''.join(s)

        words = s.split(' ')
        res = []
        for word in words:
            word = _reverse_string(list(word))
            res.append(word)

        return ' '.join(res)

    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
