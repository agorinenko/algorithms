from typing import List


def test_1():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return generate(numRows)


def generate(num_rows: int) -> List[List[int]]:
    triangle = []
    memory = {}
    for i in range(num_rows):
        row = []
        for j in range(i + 1):
            row.append(calculate_cell(i, j, memory))

        triangle.append(row)

    return triangle


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
