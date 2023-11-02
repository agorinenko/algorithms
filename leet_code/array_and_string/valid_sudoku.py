import collections
from typing import List, Tuple


def test_1():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert Solution().isValidSudoku(board)


def test_2():
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert not Solution().isValidSudoku(board)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        center_points = [(1, 1), (1, 4), (1, 7),
                         (4, 1), (4, 4), (4, 7),
                         (7, 1), (7, 4), (7, 7), ]
        return validate_rows(board) and validate_cols(board) and all(
            validate_square(board, point) for point in center_points)

def validate_square(board: List[List[str]], center_point: Tuple[int, int]) -> bool:
    x = center_point[0]
    y = center_point[1]
    vals = [
        board[x - 1][y - 1],
        board[x - 1][y],
        board[x - 1][y + 1],
        board[x][y - 1],
        board[x][y],
        board[x][y + 1],
        board[x + 1][y - 1],
        board[x + 1][y],
        board[x + 1][y + 1],
    ]
    return validate_list(vals)


def validate_rows(board: List[List[str]]) -> bool:
    for row in board:
        if not validate_list(row):
            return False

    return True


def validate_cols(board: List[List[str]]) -> bool:
    for i in range(len(board[0])):
        coll = [row[i] for row in board]
        if not validate_list(coll):
            return False

    return True


def validate_list(items: List[str]) -> bool:
    tmp = set()
    for cell in items:
        if cell == '.':
            continue

        if cell in tmp:
            return False

        tmp.add(cell)

    return True
