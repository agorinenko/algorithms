from typing import List


def test_1():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    assert Solution().floodFill(image, sr, sc, color) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


def test_2():
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    color = 0
    assert Solution().floodFill(image, sr, sc, color) == [[0, 0, 0], [0, 0, 0]]


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target_color = image[sr][sc]
        flood_fill(image, sr, sc, color, target_color)

        return image


def flood_fill(image: List[List[int]], x: int, y: int, color: int, target_color: int):
    """
    x - rows
    y - cols
    """
    if x >= 0 and y >= 0 and x < len(image) and y < len(image[0]) and image[x][y] != color and image[x][y] == target_color:
        image[x][y] = color

        flood_fill(image, x - 1, y, color, target_color)
        flood_fill(image, x + 1, y, color, target_color)
        flood_fill(image, x, y - 1, color, target_color)
        flood_fill(image, x, y + 1, color, target_color)
