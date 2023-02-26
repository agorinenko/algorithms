"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/

https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
"""
from typing import List


def test_reverse_arr():
    arr = [1, 2, 3, 4, 5, 6]
    arr = reverse_arr(arr)
    print(arr)


def reverse_arr(arr: List[int]) -> list:
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


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
