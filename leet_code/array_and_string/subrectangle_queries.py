from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


def test_1():
    [[3, 0, 3, 2, 10], [3, 1],
     [0, 2]]
    obj = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    assert 1 == obj.getValue(0, 2)
    obj.updateSubrectangle(0, 0, 3, 2, 5)
    assert 5 == obj.getValue(0, 2)
    assert 5 == obj.getValue(3, 1)
