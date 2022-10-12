from leet_code.fun_with_arrays.remove_element import Solution


def test_main_1():
    nums = [3, 2, 2, 3]
    val = 3
    assert Solution().remove_element(nums, val) == 2
    assert [2, 2, 0, 0] == nums


def test_main_2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    assert Solution().remove_element(nums, val) == 5
    assert sorted([0, 1, 4, 0, 3, 0, 0, 0], reverse=True) == sorted(nums, reverse=True)
