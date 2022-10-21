"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
"""
from typing import List


class Solution:
    def pascals_triangle(self, num_rows: int) -> List[List[int]]:
        if num_rows == 0:
            return []

        triangle = [[1]]

        if num_rows == 1:
            return triangle

        for row_idx in range(1, num_rows):
            row = [1]
            prev_row = triangle[row_idx - 1]

            for i in range(row_idx - 1):
                row.append(prev_row[i] + prev_row[i + 1])

            row.append(1)

            triangle.append(row)

        return triangle
        ''
