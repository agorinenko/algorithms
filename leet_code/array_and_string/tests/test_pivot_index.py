from leet_code.array_and_string.pivot_index import Solution


def test_main_1():
    nums = [1, 7, 3, 6, 5, 6]

    idx = Solution().pivot_index(nums)
    assert 3 == idx


def test_main_2():
    nums = [1, 2, 3]

    idx = Solution().pivot_index(nums)
    assert -1 == idx


def test_main_3():
    nums = [2, 1, -1]

    idx = Solution().pivot_index(nums)
    assert 0 == idx
