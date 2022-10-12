from leet_code.fun_with_arrays.check_if_n_and_its_double_exist import Solution


def test_main_1():
    nums = [10, 2, 5, 3]
    assert Solution().check_if_exist(nums) == True


def test_main_2():
    nums = [3,1,7,11]
    assert Solution().check_if_exist(nums) == False
