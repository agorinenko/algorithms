from collections import deque
from typing import List


def test_1():
    assert Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


def test_2():
    assert Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]


def test_3():
    assert Solution().updateMatrix([
        [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
    ]) == [
               [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
               [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
               [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
               [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
               [1, 0, 0, 0, 1, 2, 1, 1, 0, 1],
               [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
               [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]
           ]


def test_4():
    assert Solution().updateMatrix(
        [[0, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 2, 2, 1], [1, 1, 1, 0, 0, 1, 2, 3, 1, 0],
         [0, 1, 2, 1, 0, 1, 2, 3, 2, 1], [0, 0, 1, 2, 1, 2, 1, 2, 1, 0], [1, 1, 2, 3, 2, 1, 0, 1, 1, 1],
         [0, 1, 2, 3, 3, 1, 1, 0, 0, 1], [1, 2, 1, 2, 1, 0, 0, 1, 1, 2], [0, 1, 0, 1, 1, 0, 1, 2, 2, 3],
         [1, 2, 1, 0, 1, 0, 1, 2, 3, 4]]) == [[0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                                              [1, 0, 0, 1, 0, 1, 1, 2, 2, 1],
                                              [1, 1, 1, 0, 0, 1, 2, 2, 1, 0],
                                              [0, 1, 2, 1, 0, 1, 2, 3, 2, 1],
                                              [0, 0, 1, 2, 1, 2, 1, 2, 1, 0],
                                              [1, 1, 2, 3, 2, 1, 0, 1, 1, 1],
                                              [0, 1, 2, 3, 2, 1, 1, 0, 0, 1],
                                              [1, 2, 1, 2, 1, 0, 0, 1, 1, 2],
                                              [0, 1, 0, 1, 1, 0, 1, 2, 2, 3],
                                              [1, 2, 1, 0, 1, 0, 1, 2, 3, 4]]


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque([])
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()

            if r - 1 >= 0 and mat[r - 1][c] == -1:
                mat[r - 1][c] = mat[r][c] + 1
                q.append((r - 1, c))

            if r + 1 < len(mat) and mat[r + 1][c] == -1:
                mat[r + 1][c] = mat[r][c] + 1
                q.append((r + 1, c))

            if c - 1 >= 0 and mat[r][c - 1] == -1:
                mat[r][c - 1] = mat[r][c] + 1
                q.append((r, c - 1))

            if c + 1 < len(mat[0]) and mat[r][c + 1] == -1:
                mat[r][c + 1] = mat[r][c] + 1
                q.append((r, c + 1))

        return mat
