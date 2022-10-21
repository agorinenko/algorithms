"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
"""
from leet_code.array_and_string.reverse_string import Solution


def test_main_1():
    s = ["h", "e", "l", "l", "o"]
    Solution().reverse_string(s)
    assert ["o","l","l","e","h"] == s

def test_main_2():
    s = ["H","a","n","n","a","h"]
    Solution().reverse_string(s)
    assert ["h","a","n","n","a","H"] == s
