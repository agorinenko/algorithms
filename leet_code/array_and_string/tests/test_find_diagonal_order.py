from leet_code.array_and_string.find_diagonal_order import Solution


def test_main_1():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    out = Solution().find_diagonal_order(mat)
    assert [1, 2, 4, 7, 5, 3, 6, 8, 9] == out
