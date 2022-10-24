"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/
"""
from typing import List


class Solution:
    def reverse_words(self, s: str) -> str:
        def reverse_array(arr: List[str]) -> None:
            i = 0
            j = len(arr) - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        words = [i for i in s.split(' ') if i]
        reverse_array(words)
        return ' '.join(words)



