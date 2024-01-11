from typing import List


def test_1():
    assert Solution().findMatrix([1, 3, 4, 1, 2, 3, 1]) == [[1, 3, 4, 2], [1, 3], [1]]


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = []
        used_idx = set()

        while len(used_idx) < len(nums):
            row = set()
            for idx, num in enumerate(nums):
                if idx not in used_idx:
                    if num not in row:
                        row.add(num)
                        used_idx.add(idx)

            if row:
                matrix.append(list(row))

        return matrix
