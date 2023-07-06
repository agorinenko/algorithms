"""
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1380/
"""
from collections import deque
from typing import List


def test_main1():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert 3 == Solution().numIslands(grid)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count


def dfs(grid: List[List[str]], i: int, j: int):
    # un bound
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    # visited
    if int(grid[i][j]) == -1:
        return
    # An island is surrounded by water
    if int(grid[i][j]) != 1:
        return

    # mark is visited
    grid[i][j] = '-1'

    # Recur for 4 neighbours
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)
