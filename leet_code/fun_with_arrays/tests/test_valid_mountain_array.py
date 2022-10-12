from leet_code.fun_with_arrays.valid_mountain_array import Solution


def test_main_1():
    nums = [2, 1]
    assert Solution().valid_mountain_array(nums) == False


def test_main_2():
    nums = [3, 5, 5]
    assert Solution().valid_mountain_array(nums) == False


def test_main_3():
    nums = [0, 3, 2, 1]
    assert Solution().valid_mountain_array(nums) == True


def test_main_4():
    nums = [1, 7, 9, 5, 4, 1, 2]
    assert Solution().valid_mountain_array(nums) == False
