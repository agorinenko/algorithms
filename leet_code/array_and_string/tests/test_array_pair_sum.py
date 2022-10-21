from leet_code.array_and_string.array_pair_sum import Solution


def test_main_1():
    nums = [6, 2, 6, 5, 1, 2]
    res = Solution().array_pair_sum(nums)
    assert 9 == res
