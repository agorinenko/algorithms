from leet_code.array_and_string.min_sub_array_len import Solution


def test_main_1():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    res = Solution().min_sub_array_len(target, nums)
    assert 2 == res


def test_main_2():
    target = 4
    nums = [1, 4, 4]
    res = Solution().min_sub_array_len(target, nums)
    assert 1 == res


def test_main_3():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    res = Solution().min_sub_array_len(target, nums)
    assert 0 == res

def test_main_4():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    res = Solution().min_sub_array_len(target, nums)
    assert 0 == res