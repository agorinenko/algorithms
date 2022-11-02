"""
https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/
"""
from typing import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        def _get_group(x, y):
            # 0, 1, 2
            if x in [0, 1, 2]:
                if y in [0, 1, 2]:
                    return 0
                if y in [3, 4, 5]:
                    return 1
                if y in [6, 7, 8]:
                    return 2
            # 3, 4, 5
            if x in [3, 4, 5]:
                if y in [0, 1, 2]:
                    return 3
                if y in [3, 4, 5]:
                    return 4
                if y in [6, 7, 8]:
                    return 5
            # 6, 7, 8
            if x in [6, 7, 8]:
                if y in [0, 1, 2]:
                    return 6
                if y in [3, 4, 5]:
                    return 7
                if y in [6, 7, 8]:
                    return 8

        data = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in data:
                        data[board[i][j]].append((i, j))
                    else:
                        data[board[i][j]] = [(i, j)]

        for coord in data.values():
            x_list = []
            y_list = []
            groups = set()
            for i in coord:
                x_list.append(i[0])
                y_list.append(i[1])

                group = _get_group(i[0], i[1])
                if group in groups:
                    return False

                groups.add(group)

            x_set = set(x_list)
            if len(x_set) < len(x_list):
                return False

            y_set = set(y_list)
            if len(y_set) < len(y_list):
                return False

        return True
