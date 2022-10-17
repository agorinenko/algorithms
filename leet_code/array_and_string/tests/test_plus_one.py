from leet_code.array_and_string.plus_one import Solution


def test_main_1():
    nums = [1, 2, 3]

    res = Solution().plus_one(nums)
    assert [1, 2, 4] == res
