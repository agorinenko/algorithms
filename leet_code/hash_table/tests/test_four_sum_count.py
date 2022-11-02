from leet_code.hash_table.four_sum_count import Solution


def test_main_1():
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    assert Solution().four_sum_count(nums1, nums2, nums3, nums4) == 2
