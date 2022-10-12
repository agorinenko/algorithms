from leet_code.fun_with_arrays.merge_sorted_array import Solution


def test_main_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    assert [1, 2, 2, 3, 5, 6] == nums1


def test_main_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    assert [1] == nums1


def test_main_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    assert [1] == nums1
