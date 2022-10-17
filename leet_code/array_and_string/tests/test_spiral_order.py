from leet_code.array_and_string.spiral_order import Solution


def test_main_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    res = Solution().spiral_order(matrix)
    assert [1, 2, 3, 6, 9, 8, 7, 4, 5] == res


def test_main_2():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    res = Solution().spiral_order(matrix)
    assert [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] == res


def test_main_3():
    matrix = [[3], [2]]

    res = Solution().spiral_order(matrix)
    assert [3, 2] == res


def test_main_4():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    res = Solution().spiral_order(matrix)
    assert [1, 2, 3, 6, 9, 8, 7, 4, 5] == res
