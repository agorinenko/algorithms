from leet_code.array_and_string.dominant_index import Solution


def test_main_1():
    nums = [3, 6, 1, 0]

    idx = Solution().dominant_index(nums)
    assert 1 == idx


def test_main_2():
    nums = [1, 2, 3, 4]

    idx = Solution().dominant_index(nums)
    assert -1 == idx


def test_main_3():
    nums = [2, 0, 0, 3]

    idx = Solution().dominant_index(nums)
    assert -1 == idx
