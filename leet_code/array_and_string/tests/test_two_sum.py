"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
"""
import timeit

from leet_code.array_and_string.two_sum import Solution


def test_main():
    def f1(nums):
        array1 = []
        array2 = []
        for item in nums:
            if item % 2 == 0:
                array1.append(item)
            else:
                array2.append(item)

    def f2(nums):
        array1 = [i for i in nums if i % 2 == 0]
        array2 = [i for i in nums if i % 2 != 0]

    res = [i for i in range(1_000_000)]
    t1 = timeit.timeit(lambda: f1(res), number=1000)
    t2 = timeit.timeit(lambda: f2(res), number=1000)

    print(f'f1: {t1}')
    print(f'f2: {t2}')


def test_main_1():
    res = Solution().two_sum([2, 7, 11, 15], 9)
    assert res == [1, 2]


def test_main_2():
    res = Solution().two_sum([2, 3, 4], 6)
    assert res == [1, 3]


def test_main_3():
    res = Solution().two_sum([-1, 0], -1)
    assert res == [1, 2]
