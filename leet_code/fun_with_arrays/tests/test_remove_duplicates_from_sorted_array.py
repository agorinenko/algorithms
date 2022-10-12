from leet_code.fun_with_arrays.remove_duplicates_from_sorted_array import Solution


def test_main_1():
    nums = [1, 1, 2]
    assert Solution().remove_duplicates(nums) == 2
    assert [1, 2] == nums[:2]


def test_main_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert Solution().remove_duplicates(nums) == 5
    assert [0, 1, 2, 3, 4] == nums[:5]


def test_main_3():
    nums = [1]
    assert Solution().remove_duplicates(nums) == 1
    assert [1] == nums


def test_main_5():
    nums = [1, 1]
    assert Solution().remove_duplicates(nums) == 1
    assert [1] == nums[:1]


def test_main_6():
    nums = [1, 2]
    assert Solution().remove_duplicates(nums) == 2
    assert [1, 2] == nums
