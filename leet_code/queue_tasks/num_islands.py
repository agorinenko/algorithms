"""
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/
"""
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '#'
                    self.helper(grid, i, j)
                    count += 1
        return count

    # use a helper function to flip connected '1's to 0
    def helper(self, grid, i, j):
        queue = deque([(i, j)])
        while queue:
            I, J = queue.popleft()
            for i, j in [I + 1, J], [I, J + 1], [I - 1, J], [I, J - 1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '#'
                    queue.append((i, j))
