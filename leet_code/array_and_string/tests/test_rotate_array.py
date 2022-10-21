from leet_code.array_and_string.rotate_array import Solution


def test_main_1():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    Solution().rotate(nums, k)
    assert nums == [7, 1, 2, 3, 4, 5, 6]


def test_main_2():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    Solution().rotate(nums, k)
    assert nums == [6, 7, 1, 2, 3, 4, 5]


def test_main_3():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 4
    Solution().rotate(nums, k)
    assert nums == [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]

def test_main_4():
    nums = [1, 2]
    k = 3
    Solution().rotate(nums, k)
    assert nums == [2,1]

def test_main_5():
    nums = [1, 2]
    k = 2
    Solution().rotate(nums, k)
    assert nums == [1, 2]

def test_main_6():
    nums = [1,2,3]
    k = 4
    Solution().rotate(nums, k)
    assert nums == [3, 1, 2]