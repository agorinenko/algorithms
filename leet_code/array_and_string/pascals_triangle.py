"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
"""
from typing import List


class Solution:
    def get_row(self, row_index: int) -> List[int]:
        if row_index == 0:
            return [1]

        if row_index == 1:
            return [1, 1]

        prev_row = [1]

        for row_idx in range(1, row_index+1):
            row = [1]

            for i in range(row_idx - 1):
                row.append(prev_row[i] + prev_row[i + 1])

            row.append(1)

            prev_row = row

            if row_idx == row_index:
                return prev_row

        return prev_row

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
