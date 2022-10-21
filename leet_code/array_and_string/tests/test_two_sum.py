"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
"""
from leet_code.array_and_string.two_sum import Solution


def test_main_1():
    res = Solution().two_sum([2, 7, 11, 15], 9)
    assert res == [1, 2]

def test_main_2():
    res = Solution().two_sum([2,3,4], 6)
    assert res == [1, 3]

def test_main_3():
    res = Solution().two_sum([-1,0], -1)
    assert res == [1, 2]
