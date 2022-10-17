"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
"""
from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        row = 0
        col = 0
        # 0 - right
        # 1 - down
        # 2 - left
        # 3 - up

        direction = 0

        right_bound = len(matrix[0]) - 1
        left_bound = 0
        top_bound = 0
        bottom_bound = len(matrix) - 1
        total_steps = len(matrix[0]) * len(matrix)

        res = [matrix[0][0]]
        for _ in range(1, total_steps):
            if direction == 0:
                col += 1
                if col > right_bound:
                    row += 1

                if col >= right_bound:
                    col = right_bound
                    direction = 1
                    top_bound += 1
            elif direction == 1:
                row += 1
                if row > bottom_bound:
                    col -= 1

                if row >= bottom_bound:
                    row = bottom_bound
                    direction = 2
                    right_bound -= 1
            elif direction == 2:
                col -= 1
                if col < left_bound:
                    row -= 1

                if col <= left_bound:
                    col = left_bound
                    direction = 3
                    bottom_bound -= 1
            elif direction == 3:
                row -= 1
                if row < top_bound:
                    col += 1

                if row <= top_bound:
                    row = top_bound
                    direction = 0
                    left_bound += 1
            else:
                raise NotImplementedError(direction)

            res.append(matrix[row][col])

        return res
