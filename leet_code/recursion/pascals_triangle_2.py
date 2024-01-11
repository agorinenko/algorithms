from typing import List


def test_1():
    assert Solution().getRow(3) == [1, 3, 3, 1]


def test_2():
    assert Solution().getRow(4) == [1, 4, 6, 4, 1]


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle_row = []
        memory = {}
        for j in range(rowIndex + 1):
            triangle_row.append(calculate_cell(rowIndex, j, memory))

        return triangle_row


def calculate_cell(i: int, j: int, memory: dict) -> int:
    coordinate = (i, j)
    if coordinate in memory:
        return memory[coordinate]
    # Базовый случай
    if j == 0 or i == j:
        memory[coordinate] = 1
        return 1
    # рекуррентное соотношение
    result = calculate_cell(i - 1, j - 1, memory) + calculate_cell(i - 1, j, memory)
    memory[coordinate] = result
    return result
