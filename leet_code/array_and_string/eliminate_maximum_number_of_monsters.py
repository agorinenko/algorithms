from typing import List


def test_1():
    dist = [1, 3, 4]
    speed = [1, 1, 1]
    assert Solution().eliminateMaximum(dist, speed) == 3


def test_2():
    dist = [1, 1, 2, 3]
    speed = [1, 1, 1, 1]
    assert Solution().eliminateMaximum(dist, speed) == 1


def test_3():
    dist = [3, 2, 4]
    speed = [5, 3, 2]
    assert Solution().eliminateMaximum(dist, speed) == 1


def test_4():
    dist = [4, 2, 3]
    speed = [2, 1, 1]
    assert Solution().eliminateMaximum(dist, speed) == 3


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        need_minutes = [-1 for _ in range(len(dist))]
        for i in range(len(dist)):
            need_minutes[i] = dist[i] / speed[i]

        need_minutes.sort()

        c = 0
        for i in range(len(need_minutes)):
            if need_minutes[i] <= i:
                break
            c += 1
        return c
