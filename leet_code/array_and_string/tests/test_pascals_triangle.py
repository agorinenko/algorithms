from leet_code.array_and_string.pascals_triangle import Solution


def test_main_1():
    res = Solution().pascals_triangle(5)
    assert [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]] == res
