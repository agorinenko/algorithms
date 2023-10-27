from typing import List


def test_1():
    a=([], )
    print(hash(a))
    assert Solution().countNegatives([[3, 2], [1, 0]]) == 0


def test_2():
    assert Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def _check(mid, row):
            return row[mid] < 0

        ans = 0
        for row in grid:
            l = len(row)
            idx = binary_search(0, l - 1, _check, row)
            if idx == (l - 1):
                if row[idx] < 0:
                    ans += 1
            else:
                ans += l - idx
        return ans


def binary_search(left: int, right: int, check, *args):
    """ Плохо - хорошо """
    while left < right:
        mid = (left + right) // 2
        if check(mid, *args):
            right = mid
        else:
            left = mid + 1

    return left
