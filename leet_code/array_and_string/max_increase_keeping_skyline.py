from typing import List


def test_1():
    assert Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]) == 35


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        result = 0
        for r in range(n):
            for c in range(n):
                cell = grid[r][c]

                max_in_row = max(grid[r])
                max_in_col = max([row[c] for row in grid])

                result += min(max_in_row - cell, max_in_col - cell)

        return result
